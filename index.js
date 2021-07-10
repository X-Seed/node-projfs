var nodeProj = require('bindings')('NativeExtension');

// create a virtual file system
virtFS = nodeProj({
    root: "C://Program Files/Steam/steamapp/common/...",
})

// signup for each callback
virtFS.GetDirectoryEnumerationCallback = function(){
    
}
virtFS.GetFileDataCallback = function(infoObj, byteOffset, length){
    infoObj.filePathName
    infoObj.dataStreamId 
    virtFS.writeFileData(dataStreamId, Buffer.from("1234"));
}

//start virtualizing
virtFS.start()



// Future work
// nodeProj.pipeFileStream(dataStreamId, ReadableStream stream)

module.exports = NativeExtension;
