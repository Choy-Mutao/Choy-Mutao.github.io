function move_zero(nums: []) {
    return nums.sort((a,b) => Number(!a) - Number(!b));
}