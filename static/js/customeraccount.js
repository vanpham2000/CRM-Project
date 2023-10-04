function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i, j, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows
  for (i = 0; i < tr.length; i++) {
    // Initialize an array to store whether each column contains the search filter
    var match = [];

    // Loop through each column (td element) in the current row
    for (j = 0; j < tr[i].cells.length; j++) {
      td = tr[i].cells[j];
      if (td) {
        txtValue = td.textContent || td.innerText;
        // Check if the column value contains the search filter
        match.push(txtValue.toUpperCase().indexOf(filter) > -1);
      }
    }

    // If any column matches the filter, display the row; otherwise, hide it
    if (match.includes(true)) {
      tr[i].style.display = "";
    } else {
      tr[i].style.display = "none";
    }
  }
}

// Define variables
var currentPage = 1; // Current page number
var itemsPerPage = 10; // Number of items to display per page
var totalRecords = document.querySelectorAll("#myTable tbody tr").length; // Total number of records

// Function to show items for the given page
function showPage(pageNumber) {
    var tableRows = document.querySelectorAll("#myTable tbody tr");
    var startIndex = (pageNumber - 1) * itemsPerPage;
    var endIndex = startIndex + itemsPerPage;

    for (var i = 0; i < tableRows.length; i++) {
        if (i >= startIndex && i < endIndex) {
            tableRows[i].style.display = "table-row";
        } else {
            tableRows[i].style.display = "none";
        }
    }
}

// Function to handle clicking on page numbers or navigation buttons
document.querySelector(".pagination").addEventListener("click", function (e) {
    if (e.target && e.target.matches(".page-number")) {
        // Clicked on a page number
        var pageNumber = parseInt(e.target.textContent);
        currentPage = pageNumber;
        showPage(pageNumber);
        updatePaginationUI();
    } else if (e.target && e.target.id === "prev-page") {
        // Clicked on the previous page button
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
            updatePaginationUI();
        }
    } else if (e.target && e.target.id === "next-page") {
        // Clicked on the next page button
        var totalPages = Math.ceil(totalRecords / itemsPerPage);
        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
            updatePaginationUI();
        }
    }
});

// Function to update the pagination UI (active page)
function updatePaginationUI() {
    var pageNumbers = document.querySelectorAll(".page-number");
    pageNumbers.forEach(function (pageNumberElement) {
        pageNumberElement.classList.remove("active");
        if (parseInt(pageNumberElement.textContent) === currentPage) {
            pageNumberElement.classList.add("active");
        }
    });
}

// Function to check and update pagination when records are added
function checkAndUpdatePagination() {
    totalRecords = document.querySelectorAll("#myTable tbody tr").length;
    var totalPages = Math.ceil(totalRecords / itemsPerPage);
    if (currentPage > totalPages) {
        currentPage = totalPages;
        showPage(currentPage
