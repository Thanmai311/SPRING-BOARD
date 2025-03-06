burger=document.querySelector('.burger')
navbarItems=document.querySelector('.navbar-items')
nav=document.querySelector('.nav')

burger.addEventListener('click',()=>{
   navbarItems.classList.toggle('h-class')
   nav.classList.toggle('v-class')
})

// Open Popup
function openPopup() {
   document.getElementById('popup').style.display = 'block';
   document.getElementById('overlay').style.display = 'block';
}

// Close Popup
function closePopup() {
   document.getElementById('popup').style.display = 'none';
   document.getElementById('overlay').style.display = 'none';
   document.getElementById('bmiResult').style.display = 'none';
}

