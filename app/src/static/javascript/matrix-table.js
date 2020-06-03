const matrixSizeInput = document.getElementById("matrix-size-input");
window.onload = () => {
  matrixSizeInput.addEventListener("keyup", (event) => {
    debugger;

    const matrixTable = document.getElementById("matrix-table");
    matrixTable.innerHTML = "";

    const matrixSizeInputValue = !isNaN(event.target.value)
      ? parseInt(event.target.value)
      : "";

    matrixSizeInput.value = matrixSizeInputValue;
    debugger;
    if (Number.isInteger(matrixSizeInputValue)) {
      for (let i = 1; i <= matrixSizeInputValue; i++) {
        const row = document.createElement("tr");
        debugger;
        for (let j = 1; j - 1 <= matrixSizeInputValue; j++) {
          debugger;
          const cell = document.createElement("td");
          const input = document.createElement("input");
          input.setAttribute("name", i + "-" + j);
          input.setAttribute("style", "width: 40px;");
          input.setAttribute("placeholder", "0");

          cell.appendChild(input);
          row.appendChild(cell);
          matrixTable.appendChild(row);
        }
      }
    }
  });
};
