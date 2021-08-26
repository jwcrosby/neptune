const startDateInput = document.getElementById("id_start_date");
const endDateInput = document.getElementById("id_end_date");

const startPicker = MCDatepicker.create({
  el: "#id_start_date",
  dateFormat: "yyyy-mm-dd",
  closeOnBlur: true,
  selectedDate: new Date(),
  autoClose: true,
});

const endPicker = MCDatepicker.create({
  el: "#id_end_date",
  dateFormat: "yyyy-mm-dd",
  closeOnBlur: true,
  selectedDate: new Date(),
  autoClose: true,
});

startDateInput.addEventListener("click", (evt) => {
  startPicker.open();
});

endDateInput.addEventListener("click", (evt) => {
  endPicker.open();
});