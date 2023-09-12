#!/usr/bin/node

exports.esrever = function (list) {
    const current = [];
    for (let i = list.length - 1; i >= 0; i--) {
      current.push(list[i]);
    }
  
    return (current);
  };