// see https://en.wikipedia.org/wiki/Patience_sorting

var lengthOfLIS = function(nums) {
    var dp = [nums[0]];
    var lowerBound = function(val) {
        if(val > dp[dp.length - 1]) return dp.length;
        var lo  = 0;
        var hi = dp.length - 1;
        var mid;
        while(lo < hi) {
            mid = (lo + hi) / 2 | 0;
            if(dp[mid] > val) {
                hi = mid;
            } else if(dp[mid] < val) {
                lo = mid + 1;
            } else {
                return mid;
            }
        }
        return lo;
    }
    for(var i = 1; i < nums.length; i++) {
        var insertIndex = lowerBound(nums[i]);
        if(insertIndex === dp.length) dp.push(nums[i]);
        else if(dp[insertIndex] > nums[i]) dp[insertIndex] = nums[i];
    }
    return dp.length;
}
