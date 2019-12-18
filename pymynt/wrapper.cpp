#include <iostream>

#define WITH_OPENCV
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <mynteyed/camera.h>
#include <mynteyed/utils.h>

#include "util/cam_utils.h"
#include "util/counter.h"
#include "util/cv_painter.h"

MYNTEYE_USE_NAMESPACE

Camera cam;
OpenParams params;

cv::Mat getDepthImage(){
  auto image_depth = cam.GetStreamData(ImageType::IMAGE_DEPTH);
  if (image_depth.img) {
    if(params.depth_mode==DepthMode::DEPTH_GRAY){
      cv::Mat depth = image_depth.img->ToMat();
      return depth;
    }else if(params.depth_mode==DepthMode::DEPTH_RAW){
      cv::Mat depth = image_depth.img->To(ImageFormat::DEPTH_RAW)->ToMat();
      return depth;
    }else if(params.depth_mode==DepthMode::DEPTH_COLORFUL){
      auto depth_img = image_depth.img->To(ImageFormat::COLOR_BGR);
      cv::Mat depth(depth_img->height(), depth_img->width(), CV_8UC3,
          depth_img->data());
      return depth;
    }
  }else{
    std::cout << "Get Depth Image failed" << std::endl << std::endl;
    cv::Mat m(1,1,CV_8UC3);
    return m;
  }
}



int init(int depth_mode) {
  DeviceInfo dev_info;
  if (!util::select(cam, &dev_info)) {
    return 1;
  }
  util::print_stream_infos(cam, dev_info.index);

  std::cout << "Open device: " << dev_info.index << ", "
    << dev_info.name << std::endl << std::endl;

  params = OpenParams(dev_info.index);
  params.dev_mode = DeviceMode::DEVICE_DEPTH;
  params.depth_mode = static_cast<DepthMode>(depth_mode);
  params.stream_mode = StreamMode::STREAM_1280x720;
  params.ir_intensity = 4;
  params.framerate = 60;
  cam.Open(params);

  std::cout << std::endl;
  if (!cam.IsOpened()) {
    std::cerr << "Error: Open camera failed" << std::endl;
    return 1;
  }
  std::cout << "Open device success" << std::endl << std::endl;

  return 0;
}

int main(){
  init(1);

  std::cout << "Press ESC/Q on Windows to terminate" << std::endl;
  

  cv::namedWindow("depth");
  cv::Mat depth = getDepthImage();
  cv::imshow("depth", depth);
  cv::waitKey(-1);

  cv::destroyAllWindows();
  cam.Close();
  return 0;
}