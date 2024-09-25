var sortOrder = {}; // Track sorting order for each column

function sortTable(columnIndex) {
    var table = document.getElementById("patientTable");
    var rows = Array.from(table.rows);
    var order = sortOrder[columnIndex] || 'asc';

    var sortedRows = rows.sort((a, b) => {
        var aText = a.cells[columnIndex].innerText.toLowerCase();
        var bText = b.cells[columnIndex].innerText.toLowerCase();
        return order === 'asc' ? aText.localeCompare(bText) : bText.localeCompare(aText);
    });

    table.innerHTML = "";
    sortedRows.forEach(row => {
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
                header.classList.add('sorted'); // Add sorted class to the header
            } else {
                header.classList.remove('sorted'); // Remove sorted class from other headers
            }
        }
    });
}

function confirmDelete() {
    return confirm('Are you sure you want to delete this patient?');
}

function toggleSelectAll() {
    var selectAllCheckbox = document.getElementById('selectAll');
    var checkboxes = document.querySelectorAll('.selectPatient');
    checkboxes.forEach(checkbox => {
        checkbox.checked = selectAllCheckbox.checked;
    });
    toggleDeleteButton();
}

function toggleDeleteButton() {
    var checkboxes = document.querySelectorAll('.selectPatient:checked');
    var deleteButton = document.getElementById('deleteSelectedButton');
    if (checkboxes.length > 0) {
        deleteButton.style.display = 'inline-block';
    } else {
        deleteButton.style.display = 'none';
    }
}

function deleteSelectedPatients() {
    if (confirm('Are you sure you want to delete the selected patients?')) {
        var selectedPatients = [];
        var checkboxes = document.querySelectorAll('.selectPatient:checked');
        checkboxes.forEach(checkbox => {
            selectedPatients.push(checkbox.value);
        });
        if (selectedPatients.length > 0) {
            document.getElementById('patientIds').value = selectedPatients.join(',');
            document.getElementById('deleteSelectedForm').submit();
        } else {
            alert('No patients selected.');
        }
    }
}

window.onscroll = function() {
    var backToTopButton = document.getElementById('backToTop');
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        backToTopButton.style.display = 'block';
    } else {
        backToTopButton.style.display = 'none';
    }
};

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}