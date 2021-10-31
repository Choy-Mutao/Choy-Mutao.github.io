export class BinaryTreeNode {
    private _left: BinaryTreeNode;
    private _right: BinaryTreeNode;
    private _data: any;

    constructor(data: any, left?: BinaryTreeNode, right?: BinaryTreeNode) {
        this._data = data;
        if (left) {
            this._left = left;
        }
        if (right) {
            this._right = right;
        }
    }

    public setLeft(left: BinaryTreeNode): boolean {
        if (this._left) return false;
        this._left = left;
        return true;
    }

    public setRight(right: BinaryTreeNode): boolean {
        if (this._right) return false;
        this._right = right;
        return true;
    }

}