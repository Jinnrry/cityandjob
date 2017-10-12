<?php
/**
 * Created by PhpStorm.
 * User: jiangwei
 * Date: 2017/10/12
 * Time: 15:06
 */

namespace app\index\model;


use think\Model;

class roomprice extends Model
{
    //得到房价信息
    public  function  getinfo($locate)
    {
        return $this->where("cityname like '%".$locate."%'")->select();
    }

    public function getinfo_none()
    {

        return $this->field("avg(price) as price ")->select();
    }





}