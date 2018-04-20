// interface Shape {
//     name: string;
//     width: number;
//     height: number;
//     color?: string;
// }
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// function area(shape : Shape) {
//     var area = shape.width * shape.height;
//     return "I'm " + shape.name + " with area " + area + " cm squared";
// }
// console.log( area( {name: "rectangle", width: 30, height: 15} ) );
// console.log( area( {name: "square", width: 30, height: 30, color: "blue"} ) );
var shape = {
    name: "rectangle",
    popup: function () {
        var _this = this;
        console.log('This is inside popup():' + this.name);
        setTimeout(function () {
            console.log('This inside setTimeout:' + _this.name);
            console.log("I'm a " + _this.name + "!");
        }, 3000);
    }
};
// shape.popup();
var Shape = /** @class */ (function () {
    function Shape(name, width, height) {
        this.name = name;
        this.area = width * height;
        this.color = "pink";
        this.name = name;
    }
    ;
    Shape.prototype.shoutout = function () {
        return "I'm" + this.color + " " + this.name + "with and area of " + this.area;
    };
    return Shape;
}());
var Shape3D = /** @class */ (function (_super) {
    __extends(Shape3D, _super);
    function Shape3D(name, width, height, length) {
        var _this = _super.call(this, name, width, height) || this;
        _this.name = name;
        _this.volume = length * _this.area;
        return _this;
    }
    Shape3D.prototype.shoutout = function () {
        return "It is " + this.name + "with a volume of " + this.volume + "cm";
    };
    Shape3D.prototype.superShout = function () {
        return _super.prototype.shoutout.call(this);
    };
    return Shape3D;
}(Shape));
// var cube = new Shape3D('cube',30,30,30);
// console.log(cube.shoutout());
// console.log(cube.superShout());
var namelzl = "name";
namelzl = "linzhilang";
var list = [1, 2, 3];
var list1 = [1, 2, 3];
var Color;
(function (Color) {
    Color[Color["Red"] = 1] = "Red";
    Color[Color["Green"] = 2] = "Green";
    Color[Color["Blue"] = 3] = "Blue";
})(Color || (Color = {}));
;
var colorName = Color[2];
alert(colorName);
alert("Hello ,my name is " + namelzl);
