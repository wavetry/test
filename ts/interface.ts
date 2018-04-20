// interface Shape {
//     name: string;
//     width: number;
//     height: number;
//     color?: string;
// }
 
// function area(shape : Shape) {
//     var area = shape.width * shape.height;
//     return "I'm " + shape.name + " with area " + area + " cm squared";
// }
 
// console.log( area( {name: "rectangle", width: 30, height: 15} ) );
// console.log( area( {name: "square", width: 30, height: 30, color: "blue"} ) );

var shape = {
	name:"rectangle",
	popup:function () {
		console.log('This is inside popup():' + this.name);
		setTimeout( ()=> {
			console.log('This inside setTimeout:' + this.name);
			console.log("I'm a " + this.name + "!");
		},3000);

	}
}

// shape.popup();

class Shape{
	area:number;
	private color:string;
	constructor(public name:string,width:number,height:number){
		this.area = width * height;
		this.color = "pink";
		this.name = name;
	};
	shoutout(){
		return "I'm" + this.color + " " + this.name + "with and area of " + this.area;	
	}

}

class Shape3D extends Shape{
	volume:number;
	constructor (public name:string,width:number,height:number,length:number){
		super(name,width,height);
		this.volume = length * this.area;
	}

	shoutout(){
		return "It is "+ this.name + "with a volume of " + this.volume + "cm";
	}

	superShout(){
		return super.shoutout();
	}
}
// var cube = new Shape3D('cube',30,30,30);
// console.log(cube.shoutout());
// console.log(cube.superShout());


let namelzl:string = `name`;
namelzl = "linzhilang";

let list:number[] = [1,2,3];
let list1:Array<number> = [1,2,3];

enum Color {Red = 1,Green,Blue};
let colorName:string = Color[2];

let suiiban:any = 5;

alert(colorName);
alert(`Hello ,my name is ${ namelzl }`);

