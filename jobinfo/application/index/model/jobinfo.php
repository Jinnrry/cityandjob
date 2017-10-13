<?php
/**
 * Created by PhpStorm.
 * User: jiangwei
 * Date: 2017/10/12
 * Time: 15:03
 */

namespace app\index\model;


use think\Model;

class jobinfo extends Model
{
    public function  getinfo($post,$locate)
    {
           return $this->field("count(1) as num, avg(salary_max)  as avgmax  ,avg(salary_min) as avgmin ,std(salary_max) as stdmax ,std(salary_min) as stdmin ")->where("locate","like","%".$locate."%")->where("post" ,"like","%".$post."%" )->select();
    }

    public function  getinfo_post($post)
    {
        return $this->field("count(1) as num, avg(salary_max)  as avgmax  ,avg(salary_min) as avgmin ,std(salary_max) as stdmax ,std(salary_min) as stdmin ")->where("post" ,"like","%".$post."%" )->select();
    }

    public function  getinfo_locate($locate)
    {
        return $this->field("count(1) as num, avg(salary_max)  as avgmax  ,avg(salary_min) as avgmin ,std(salary_max) as stdmax ,std(salary_min) as stdmin ")->where("locate","like","%".$locate."%")->select();
    }

    public function  getinfo_none()
    {
        return $this->field("count(1) as num, avg(salary_max)  as avgmax  ,avg(salary_min) as avgmin ,std(salary_max) as stdmax ,std(salary_min) as stdmin ")->select();
    }

}