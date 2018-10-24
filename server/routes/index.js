// var express = require('express');
// var router = express.Router();


const router = require('express').Router();
const multer = require('multer');
let upload = multer({ dest: 'uploads/' });
const fs = require('fs');
const path = require('path');
tasklist = [];
/* GET home page. */
// router.get('/', function(req, res, next) {
//   res.render('index', { title: 'Express' });
// });


router.post('/upload',upload.single('myFile'),(req,res,next)=>{
    if (!req.file){
      res.send("出错了");
      return ;
    }
    console.log(req.file.originalname);
    console.log(req.file.path);
    let oldPath = path.join('../','bin',req.file.path);
    // console.log(oldPath);
    let newPath = path.join('../','bin/uploads',req.file.originalname);
    fs.rename(oldPath,newPath,(err)=>{
        if (err){
        return console.log(err);}
        console.log("修改成功")
    });

    tasklist.push(newPath);
    res.send('兄弟，你的请求成功了')
});



router.get('/poll', (req, res)=>{
    if(tasklist.length==0){
        console.log(tasklist);
        res.send("notask");
        return;
    }
    var task = tasklist[0].split('\\');
    tasklist.shift();
    res.send(task[task.length-1]);

});
result_list = [];
router.get('/download/:file', (req, res)=>{

    var file=req.params.file;
    res.sendFile(file, {root: "D:\\homework\\bigProject\\server\\bin\\uploads\\"}, err => {
});});

router.get('/get/:file', (req, res)=>{
    res.set("Content-Type", "charset=utf-8");
    var file=req.params.file;
    // res.send("请下载相应的文件")
    console.log(file);
    console.log(result_list);
    if (result_list.indexOf(file)+1) {
        res.sendFile(file, {root: "D:\\homework\\bigProject\\server\\bin\\uploads\\"}, err => {
        });
    }else{
        res.end('please wait ')
    }
});
router.post('/result',upload.single("result"),(req,res,next)=>{
    if (!req.file){
        res.send("出错了");
        return ;
    }
    console.log(req.file.originalname);
    console.log(req.file.path);
    let oldPath = path.join('../','bin',req.file.path);
    // console.log(oldPath);
    let newPath = path.join('../','bin/uploads',req.file.originalname);
    fs.rename(oldPath,newPath,(err)=>{
        if (err){
            return console.log(err);}
        console.log("修改成功")
    });
    result_list.push(req.file.originalname);
    res.end()
});



module.exports = router;