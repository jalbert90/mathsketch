// Obtain references to canvas object and drawing info object
// DPR used to make drawing buffer px width of canvas match real px width of canvas
const canvas = document.getElementById("draw-canvas");
const ctx = canvas.getContext("2d");
const dpr = window.devicePixelRatio;

// Set the visible size of the canvas in CSS pixels
canvas.style.width = 280 + 'px';
canvas.style.height = 280 + 'px';

// Scale the drawing buffer so that there is 1 buffer pixel for every real screen pixel
// Draw in CSS coordinates -> maps to buffer -> buffer mapped to real screen pixels
// To avoid stretching or blending
// Assumes that viewport width is set to device-width in the HTML meta tag
canvas.width = canvas.style.width * dpr;
canvas.heigth = canvas.style.height * dpr;

// Scale all buffer coordinates so that they match the CSS coordinates
// Drawing full length of canvas in CSS units should fill the buffer
ctx.scale(dpr, dpr)

function begin_drawing() {

}

canvas.addEventListener("mousedown", )
