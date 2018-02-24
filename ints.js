'use strict'

var keepCount = 0
var timeObj = {}
var strObj = ""
var quit = {}

function displayTime(obj,str) {
  if (keepCount <= 120) {
    obj = new Date()
    str = obj.toLocaleTimeString()
    console.log("the time is ~ " + str)
    keepCount++
  } else {
    console.log("oil.boil()")
    quit = clearInterval()
  }
}

function startInterval(timeObj,strObj) {
    setInterval( function () {displayTime(timeObj, strObj)}, 1000)
}

startInterval(timeObj,strObj)
