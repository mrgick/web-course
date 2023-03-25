class RGB {
    constructor(r, g, b) {
        this.r = r
        this.g = g
        this.b = b
    }

    componentToHex(c) {
        var hex = c.toString(16);
        return hex.length == 1 ? "0" + hex : hex;
    }

    get rgb() {
        return `rgb(${this.r},${this.g},${this.b})`
    }
    get hex() {
        return "#" + componentToHex(this.r) + componentToHex(this.g) + componentToHex(this.b);
    }

    static getRandomColor(weight = 256) {
        return new RGB(
            Math.floor((Math.random() * weight)),
            Math.floor((Math.random() * weight)),
            Math.floor((Math.random() * weight))
        )
    }

    get invertColor_bw() {
        if (this.r + this.g + this.b < 255 * 2.8) {
            return new RGB(255, 255, 255)
        }
        return RGB.getRandomColor(80)
    }
}


function change_color(e, text = false) {
    let randomColor = RGB.getRandomColor();
    let invertColor = randomColor.invertColor_bw
    console.log(randomColor, invertColor)
    if (!text) {
        $(e).css("background-color", randomColor.rgb);
        $(e).css("color", invertColor.rgb);
    } else {
        $(e).css("color", randomColor.rgb);
        $(e).css("background-color", invertColor.rgb);
    }


}


$(".btn").hover((e) => change_color(e.currentTarget));
$(".form-control").hover((e) => change_color(e.currentTarget, true));
