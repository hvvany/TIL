const textInput = document.querySelector("#text-input");

textInput.addEventListener("input", function (e) {
  console.log(e);
  console.log(e.target.value);
});
