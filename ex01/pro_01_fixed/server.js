const express = require('express');
const csurf = require('csurf');
const cookieParser = require('cookie-parser');
const session = require('express-session');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();

// By default, the port 8080 will be used if the APP_PORT environment variable is not set
const PORT = process.env.APP_PORT || 8080;

// Insecure way to store balance (just for demonstration purposes)
let balance = 1000;

app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(session({
    secret: 'secret',
    resave: false,
    saveUnitialized: true,
    cookie: { secure: false }
}));
const csrfProtection = csurf({ cookie: true });

// Route to serve the index.html file when a request is made to the root URL "/"
app.get('/', csrfProtection, (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/csrf-token', csrfProtection, (req, res) => {
    res.json({ csrfToken: req.csrfToken() });
});


// Get current balance
app.get('/balance', (req, res) => {
    res.json({ balance });
});

// Transfer money (vulnerable to CSRF)
app.post('/transfer', csrfProtection, (req, res) => {
    const amount = parseInt(req.body.amount);
    if (!isNaN(amount) && amount > 0 && amount <= balance) {
        balance -= amount;
        console.log('transferred amount: ${amount, new balance: ${balance}');
        res.json({ success: true });
    } else {
        res.json({ success: false, error: 'Invalid transfer amount or insufficient balance.' });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
