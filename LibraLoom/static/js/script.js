const form = document.getElementById('book-summary-form');
const summaryResultElement = document.getElementById('summary-result');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const bookName = document.getElementById('book-name').value;
    const summaryLength = document.getElementById('summary-length').value;

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/generate-summary');
    xhr.setRequestHeader('Content-Type', 'application/json');

    const data = JSON.stringify({
        book_name: bookName,
        summary_length: summaryLength,
    });

    xhr.onload = () => {
        if (xhr.status === 200) {
            const summary = JSON.parse(xhr.responseText).summary;
            summaryResultElement.textContent = summary;
        } else {
            summaryResultElement.textContent = 'Error generating summary.';
        }
    };

    xhr.send(data);
});
