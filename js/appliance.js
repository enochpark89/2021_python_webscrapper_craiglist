let container = document.getElementById('loading');
let progress_bar = document.getElementById('progress_bar');
let btn = document.getElementById('btn');

function showbar() {
    container.style.display = 'block';
    setTimeout(changeToTenth, 3000)
}

function changeToTenth() {
  progress_bar.style = "width: 10%"
  progress_bar.innerText = "10%"
  setTimeout(changeToHundred, 15000)
}

function changeToTwentyFive() {
    progress_bar.style = "width: 25%"
    progress_bar.innerText = "25%"
    setTimeout(changeToSeventyFive, 25000)
}

function changeToSeventyFive() {
    progress_bar.style = "width: 75%"
    progress_bar.innerText = "75%"
    setTimeout(changeToHundred, 25000)
  }

function changeToHundred() {
  progress_bar.style = "width: 100%"
  progress_bar.innerText = "100%"

}

btn.addEventListener('click', showbar);