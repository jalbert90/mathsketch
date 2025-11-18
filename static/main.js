// Standardize comments.....

// Obtain references to canvas object and drawing info object
// DPR used to make drawing buffer px width of canvas match real px width of canvas
const canvas = document.getElementById("draw-canvas");
const ctx = canvas.getContext("2d");

const dpr = window.devicePixelRatio;    // Capital.....

// Set configs.....

// Set the visible size of the canvas in CSS pixels
canvas.style.width = 280 + 'px';
canvas.style.height = 280 + 'px';

// Scale the drawing buffer so that there is 1 buffer pixel for every real screen pixel
// Draw in CSS coordinates -> maps to buffer -> buffer mapped to real screen pixels
// To avoid stretching or blending
// Assumes that viewport width is set to device-width in the HTML meta tag
canvas.width = canvas.style.width * dpr;
canvas.heigth = canvas.style.height * dpr;

// Scale the buffer coordinate system to match the CSS coordinate system.
// Scaling by the devicePixelRatio ensures that drawing a full canvas size
// (in CSS units) correctly fills the underlying pixel buffer.
ctx.scale(dpr, dpr)

// Set the stroke width in CSS pixels.
// The lineWidth is originally measured in unscaled buffer pixels.
// Scaling by the DPR makes lineWidth measured in CSS pixels.
ctx.lineWidth = 5;

// Get position of mouse relative to top-left corner of canvas
// Inc y is down, inc x is right
function get_mouse_canvas_coordinates(mouse_event){
    const rect = canvas.getBoundingClientRect();
    const x = rect.left;
    const y = rect.top;
    return [x, y];
}

function begin_drawing(mouse_event) {
    const [x, y] = get_mouse_canvas_coordinates(mouse_event);
    ctx.beginPath();
}

canvas.addEventListener("mousedown", )
