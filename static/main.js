document.querySelector(".select").addEventListener("click", function () {
    document.querySelector("#open").click();
});
document.querySelector(".upload").addEventListener("click", function () {
    document.querySelector(".fileform").submit();
});

document.querySelector("#open").addEventListener("change", function () {
    document.querySelector(".filename").textContent = document.querySelector("#open").files[0].name;
});

