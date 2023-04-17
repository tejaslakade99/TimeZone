let uploadButton = document.getElementById("upload-button");
let chosenImage = document.getElementById("chosen-image");

uploadButton.onchange = () => {
    let reader = new FileReader();
    reader.readAsDataURL(uploadButton.files[0]);
    console.log(uploadButton.files[0]);
    reader.onload = () => {
        chosenImage.setAttribute("src", reader.result);
    }
}

let uploadButton2 = document.getElementById("upload-button2");
let chosenImages = document.getElementById("chosen-images");
let numFiles = document.getElementById("num-of-files")
console.log(uploadButton2,chosenImages,numFiles);

function preview() {
    chosenImages.innerHTML = "";
    if (uploadButton2.files.length !== 0){
        numFiles.textContent = `${uploadButton2.files.length}Files Selected`;
    }

    for(i of uploadButton2.files){
        let reader2 = new FileReader();
        let figure = document.createElement("figure");
        let figcap = document.createElement("figcaption");
        figcap.innerText = i.name;
        figure.appendChild(figcap);
        reader2.onload=()=>{
            let img = document.createElement("img");
            img.setAttribute("src", reader2.result);
            img.setAttribute("style","max-height: 250px;max-width: 360px;");
            img.setAttribute("class","col-md-4");
            figure.setAttribute("class","col-md-4");
            figure.insertBefore(img,figcap);
        }
        chosenImages.appendChild(figure);
        reader2.readAsDataURL(i);
    }

}

function changePrice(){
    var priceChangeTimeout = setTimeout(changePrice1,10);
}

function changePrice1(){
    let quantity = document.getElementById('product-quantity').value;
    let singleprice = document.getElementById('single-product-price').innerText;
    let finalPrice= parseFloat(singleprice) * (parseFloat(quantity));
    finalPrice = finalPrice.toFixed(2);
    document.getElementById('product-price').innerText = finalPrice;

}

document.getElementsByClassName('ti-angle-right').innerText = ">";