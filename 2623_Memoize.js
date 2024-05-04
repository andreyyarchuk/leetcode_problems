/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
	const cached = {}
	return function (...args) {
		let key = String(args)
		if (key in cached) {
			return cached[key]
		}
		let result = fn(...args)
		cached[key] = result
		return result
	}
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
