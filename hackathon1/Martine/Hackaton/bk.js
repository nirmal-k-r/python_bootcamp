// ...

// Get the calendar container and buttons
var calendar = document.querySelector(".calendar");
var prevBtn = document.getElementById("prevBtn");
var nextBtn = document.getElementById("nextBtn");

// Set initial date
var currentDate = new Date();

// Event listeners for previous and next buttons
prevBtn.addEventListener("click", showPreviousMonth);
nextBtn.addEventListener("click", showNextMonth);

// Display the calendar for the current month
displayCalendar(currentDate);

// Function to display the calendar for a specific month
function displayCalendar(date) {
  var monthYear = document.getElementById("monthYear");
  var daysContainer = document.querySelector(".days");

  // Clear the calendar
  daysContainer.innerHTML = "";

  // Set the month and year in the header
  var month = date.toLocaleString("default", { month: "long" });
  var year = date.getFullYear();
  monthYear.textContent = month + " " + year;

  // Get the first day and last day of the month
  var firstDay = new Date(date.getFullYear(), date.getMonth(), 1);
  var lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);

  // Add empty days before the first day of the month
  for (var i = 0; i < firstDay.getDay(); i++) {
    var emptyDay = document.createElement("div");
    emptyDay.classList.add("empty");
    daysContainer.appendChild(emptyDay);
  }

  // Add days to the calendar
  for (var day = 1; day <= lastDay.getDate(); day++) {
    var calendarDay = document.createElement("div");
    calendarDay.textContent = day;
    calendarDay.addEventListener("click", selectDate);
    daysContainer.appendChild(calendarDay);
  }
}

// Function to select a date
function selectDate(event) {
  var selectedDay = event.target;
  var selectedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), parseInt(selectedDay.textContent));

  // Clear previously selected dates
  var selectedDates = document.querySelectorAll(".selected");
  selectedDates.forEach(function (date) {
    date.classList.remove("selected");
  });

  // Add selected class to the clicked date
  selectedDay.classList.add("selected");

  // Perform further actions with the selected date
  console.log("Selected Date:", selectedDate);
  // ... Perform any other actions you need with the selected date
}

// Function to show the previous month
function showPreviousMonth() {
  var previousMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1);
  currentDate = previousMonth;
  displayCalendar(currentDate);
}

// Function to show the next month
function showNextMonth() {
  var nextMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1);
  currentDate = nextMonth;
  displayCalendar(currentDate);
}

// Add days to the calendar
for (var day = 1; day <= lastDay.getDate(); day++) {
    var calendarDay = document.createElement("div");
    calendarDay.textContent = day;
    
    // Create an input element for the text
    var textInput = document.createElement("input");
    textInput.type = "text";
    textInput.classList.add("event-input");
    
    // Add event listener to save the text on input change
    textInput.addEventListener("input", function(event) {
      var inputText = event.target.value;
      saveEvent(day, inputText);
    });
    
    // Append the text input to the calendar day
    calendarDay.appendChild(textInput);
    
    // Check if there is a saved event for the day
    var savedEvent = getSavedEvent(day);
    if (savedEvent) {
      textInput.value = savedEvent;
    }
    
    daysContainer.appendChild(calendarDay);
  }
  
  // Function to save the event for a specific day
  function saveEvent(day, eventText) {
    localStorage.setItem("event_" + day, eventText);
    events[day] = eventText;
  }
  
  // Function to retrieve a saved event for a specific day
  function getSavedEvent(day) {
    return localStorage.getItem("event_" + day);
  }

