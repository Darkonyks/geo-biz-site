document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.php-email-form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            let formData = new FormData(this);
            
            // Disable submit button during submission
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
            }
            
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(async (response) => {
                const raw = await response.text();
                let data = null;
                try { data = JSON.parse(raw); } catch (e) { /* nije JSON */ }

                if (!response.ok || !data) {
                    // Najčešće: server ne izvršava PHP (npr. Live Server -> 405),
                    // ili PHP ispisuje grešku umesto JSON-a.
                    let hint = 'Server status ' + response.status;
                    if (response.status === 405 || response.status === 501) {
                        hint += ' — stranica se ne servira preko PHP-a (kontakt forma radi samo na PHP serveru/hostingu).';
                    } else if (raw) {
                        hint += ': ' + raw.replace(/<[^>]+>/g, '').trim().slice(0, 200);
                    }
                    throw new Error(hint);
                }
                return data;
            })
            .then(data => {
                alert(data.message);
                if (data.success) this.reset();
            })
            .catch(error => {
                alert('Greška pri slanju poruke. ' + error.message);
                console.error('Contact form error:', error);
            })
            .finally(() => {
                // Re-enable submit button
                if (submitButton) {
                    submitButton.disabled = false;
                }
            });
        });
    });
});