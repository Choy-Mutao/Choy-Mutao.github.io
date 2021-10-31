export class MinStack {

    private stackArray: number[]

    constructor() {
        this.stackArray = []
    }

    push(x: number): void {
        this.stackArray.push(x);
    }

    pop(): void {
        this.stackArray.pop();
    }

    top(): number {
        return this.stackArray[this.stackArray.length -1];
    }

    getMin(): number {
        let min = this.stackArray[0];
        this.stackArray.forEach(num => {
            min = num < min ? num : min;
        })
        return min;
    }
}