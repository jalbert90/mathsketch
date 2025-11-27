const canvas = document.getElementById('draw-canvas');  // Canvas
const ctx = canvas.getContext('2d');                    // Drawing info
const clearButton = document.getElementById('clear-btn');

// The devicePixelRatio is used to make the drawing buffer have the same number
// of pixels as the width of the canvas in real pixels.
const DPR = window.devicePixelRatio;

// Config (CSS pixels)
const CANVAS_SIZE = 280;
const LINE_WIDTH = 50;

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
canvas.width = Math.round(CANVAS_SIZE * DPR);
canvas.height = Math.round(CANVAS_SIZE * DPR);

// Scale the buffer coordinate system to match the CSS coordinate system.
// Scaling by the devicePixelRatio ensures that drawing a full canvas size
// (in CSS units) correctly fills the underlying pixel buffer.
ctx.scale(DPR, DPR);

// Stroke config:
// Set the stroke width in CSS pixels.
// The lineWidth is originally measured in unscaled buffer pixels.
// Scaling by the DPR makes lineWidth measured in CSS pixels.
ctx.lineWidth = LINE_WIDTH;
ctx.lineCap = 'round';      // End of line shape
ctx.lineJoin = 'round';     // Line corner shape (prevents crazy long sharp edges)

// State variables:
let drawing = false;

function onClearButtonPress(event) {
    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(0, 0, CANVAS_SIZE, CANVAS_SIZE);
}

onClearButtonPress();

function beginLine(event) {
    canvas.setPointerCapture(event.pointerId);

    // Get the position of the mouse relative to top-left corner of canvas.
    // y increases downward, and x increases to the right.
    const x = event.offsetX;
    const y = event.offsetY;
    drawing = true;
    ctx.beginPath();
    ctx.moveTo(x, y);
}

function incrementLine(event) {
    if (!drawing) return;
    const x = event.offsetX;
    const y = event.offsetY;
    ctx.lineTo(x, y);
    ctx.stroke();
}

function endLine(event) {
    drawing = false;
}

canvas.addEventListener("pointerdown", beginLine);
canvas.addEventListener("pointermove", incrementLine);
canvas.addEventListener("pointerup", endLine);
clearButton.addEventListener("pointerdown", onClearButtonPress);
