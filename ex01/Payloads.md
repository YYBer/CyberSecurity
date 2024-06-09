    <form id="csrf-attack-form" action="http://localhost:8070/transfer" method="post">
        <input type="hidden" name="amount" value="100">
        <input type="hidden" name="_csrf" value="CSRF_TOKEN_PLACEHOLDER">
    </form>


    app.post('/transfer', (req, res) => {
    const amount = parseInt(req.body.amount);
    if (!isNaN(amount) && amount > 0 && amount <= balance) {
        balance -= amount;
        res.json({ success: true });
    } else {
        res.json({ success: false, error: 'Invalid transfer amount or insufficient balance.' });
    }
    });