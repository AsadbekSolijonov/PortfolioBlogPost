/*--------------------------------------------
Sahifaga har 1 min da yangilanish berish uchun
--------------------------------------------*/
setTimeout(function () {
	location.reload();
}, 60000);

/*----------------------
LocalStorage ga salqash
----------------------*/
getAuthor = document.querySelector("#author");

getAuthor.addEventListener("change", function (eve) {
	console.log(eve.target.value);
});
