<?php
namespace app\index\controller;

use app\index\model\jobinfo;
use app\index\model\roomprice;
use think\Controller;

class Index extends Controller
{
    public function index()
    {
        return $this->fetch();
    }


    public function content()
    {
        $city=input("city","全国");
        $post=input("post","全部");

        $jobinfo=new jobinfo();
        $roomprice=new roomprice();
        $roominfo=null;
        $job=null;
        if(empty($city))
        {
            $city="全国";
            $roominfo=$roomprice->getinfo_none();
        }else{
            $roominfo=$roomprice->getinfo($city);
        }
        if(empty($post))
        {
            $post="全部";
            if($city =="全国"  ){
                $job=$jobinfo->getinfo_none();
            }else{
                $job=$jobinfo->getinfo_locate($city);
            }
        }else{
            if($city =="全国"){
                $job=$jobinfo->getinfo_post($post);
            }else{
                $job=$jobinfo->getinfo($post,  $city);
            }
        }


        $this->assign("city",$city);
        $this->assign("post",$post);
        $this->assign("job",$job->toArray());
        $this->assign("room",$roominfo->toArray());


        return $this->fetch();
    }


}
