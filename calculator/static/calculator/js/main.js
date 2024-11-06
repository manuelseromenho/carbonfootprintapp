document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('carbonForm');
    const results = document.getElementById('results');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = {
            car_mileage: parseFloat(document.getElementById('car_mileage').value),
            car_fuel_type: document.getElementById('car_fuel_type').value,
        };
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('/calculator/calculate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('totalEmissions').textContent = data.total_emissions.toFixed(2);
                results.style.display = 'block';
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while calculating emissions.');
            });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
