#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, n) {
    array.push(n);
    return array;
  }, []);
};
