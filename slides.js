let slideIndex =0;
showSlides();

function shoSlides(){
	let i;
	let slides = document.getElementsByClassName("myslides")l
	for (i = 0; i < slides.length; i++){
    	slides[i].style.display = "none";
}
slideIndex++;
if (slideIndex > slides.length) {slideIndex = 1}
slides[slidesIndex -1].style.display="block;
setTimeout(showSlides,3000);
