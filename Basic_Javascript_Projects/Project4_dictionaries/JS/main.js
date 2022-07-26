//JS File for project 4 //

function quickDictionary(){
    var Plant = {
        Species: "Philodendron",
        Color: "Green",
        LightReq: "Shade",
        WaterReq: "Heavy",
        SoilReq: "Peat Moss",
        MatureHeightFeet: 6,
        MatureWidthFeet: 6,
    };
    delete Plant.LightReq;
    document.getElementById("Dictionary").innerHTML = Plant.LightReq;
}