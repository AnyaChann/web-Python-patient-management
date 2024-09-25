var sortOrder = {}; // Track sorting order for each column

function sortTable(columnIndex) {
    var table = document.getElementById("patientTable");
    var rows = Array.from(table.rows);
    var order = sortOrder[columnIndex] || 'asc';

    var sortedRows = rows.sort((a, b) => {
        var aText = a.cells[columnIndex].innerText;
        var bText = b.cells[columnIndex].innerText;
        return order === 'asc' ? aText.localeCompare(bText) : bText.localeCompare(aText);
    });

    table.innerHTML = "";
    sortedRows.forEach(row => {
        row.classList.add('sorted-row'); // Add class to sorted rows
        table.appendChild(row);
    });

    // Toggle sorting order for next click
    sortOrder[columnIndex] = order === 'asc' ? 'desc' : 'asc';

    // Update header to reflect sorting order
    updateHeader(columnIndex, sortOrder[columnIndex]);
}

function updateHeader(columnIndex, order) {
    var headers = document.querySelectorAll('th');
    headers.forEach((header, index) => {
        var icon = header.querySelector('i');
        if (icon) {
            icon.className = 'fas'; // Reset icon class
            if (index === columnIndex) {
                icon.classList.add(order === 'asc' ? 'fa-arrow-up' : 'fa-arrow-down');
            }
        }
    });
}