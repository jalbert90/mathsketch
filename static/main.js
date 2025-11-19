const canvas = document.getElementById("draw-canvas");  // Canvas
const ctx = canvas.getContext("2d");                    // Drawing info

// The devicePixelRatio is used to make the drawing buffer have the same number
// of pixels as the width of the canvas in real pixels.
const DPR = window.devicePixelRatio;

// Config (CSS pixels)
const CANVAS_SIZE = 280;
const LINE_WIDTH = 5;

// Set the visible size of the canvas in CSS pixels.
canvas.style.width = CANVAS_SIZE + 'px';
canvas.style.height = CANVAS_SIZE + 'px';

// Set the size of the drawing buffer equal to the size of the canvas in real pixels
// to avoid stretching or blending.
// # of drawing buffer pxs = # of real pxs
// Draw in CSS coordinates -> maps to buffer -> buffer mapped to real screen pixels
// **This calculation assumes that the viewport width is set to the device-width in an HTML meta tag:
// <meta name="viewport" content="width=device-width, initial-scale=1">.**
// device-width = width of screen in CSS pixels
// width = how big the browswer pretends the viewport is
canvas.width = canvas.style.width * DPR;
canvas.heigth = canvas.style.height * DPR;

// Scale the buffer coordinate system to match the CSS coordinate system.
// Scaling by the devicePixelRatio ensures that drawing a full canvas size
// (in CSS units) correctly fills the underlying pixel buffer.
ctx.scale(DPR, DPR)

// Set the stroke width in CSS pixels.
// The lineWidth is originally measured in unscaled buffer pixels.
// Scaling by the DPR makes lineWidth measured in CSS pixels.
ctx.lineWidth = 5;

function begin_drawing(event) {
    // Get the position of the mouse relative to top-left corner of canvas.
    // y increases downward, and x increases to the right.
    const x = event.offsetX;
    const y = event.offsetY;
    ctx.beginPath();
    ctx.moveTo(x, y);
}

canvas.addEventListener("mousedown", )
