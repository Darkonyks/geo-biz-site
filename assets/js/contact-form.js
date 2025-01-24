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
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    this.reset();
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                alert('An error occurred. Please try again later.');
                console.error('Error:', error);
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