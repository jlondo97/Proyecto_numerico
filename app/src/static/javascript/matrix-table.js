const matrixSizeInput = document.getElementById("matrix-size-input");
const vectorSizeInput = document.getElementById("matrix-size-input");
window.onload = () => {
  matrixSizeInput.addEventListener("keyup", (event) => {
    const matrixTable = document.getElementById("matrix-table");
    matrixTable.innerHTML = "";

    const matrixSizeInputValue = !isNaN(event.target.value)
      ? parseInt(event.target.value)
      : "";

    matrixSizeInput.value = matrixSizeInputValue;

    if (Number.isInteger(matrixSizeInputValue)) {
      for (let i = 1; i <= matrixSizeInputValue; i++) {
        const row = document.createElement("tr");

        for (let j = 1; j - 1 <= matrixSizeInputValue; j++) {
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
  vectorSizeInput.addEventListener("keyup", (event) => {
    const matrixTable = document.getElementById("valores-table");
    matrixTable.innerHTML = "";

    const matrixSizeInputValue = !isNaN(event.target.value)
      ? parseInt(event.target.value)
      : "";

    matrixSizeInput.value = matrixSizeInputValue;
    debugger;
    if (Number.isInteger(matrixSizeInputValue)) {
      const row = document.createElement("tr");
      for (let i = 1; i <= matrixSizeInputValue; i++) {
        const cell = document.createElement("td");
        const input = document.createElement("input");
        input.setAttribute("name", "x" + i);
        input.setAttribute("style", "width: 40px;");
        input.setAttribute("placeholder", "x" + i);

        cell.appendChild(input);
        row.appendChild(cell);
        matrixTable.appendChild(row);
      }
    }
  });
};
