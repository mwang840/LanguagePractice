function findPoint(px, py, qx, qy) {
    // Write your code here
    const newPtx = rotate(px, qx);
    const newPty = rotate(py, qy);
    let newPt = [];
    return newPt.push(newPtx).push(newPty);
}

function rotate(origin, rotatedPt){
    return origin + 2 * (rotatedPt - origin)
}