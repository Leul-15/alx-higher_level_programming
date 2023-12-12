#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, n) => n === searchElement ? count + 1 : count, 0);
};
