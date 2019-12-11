#include <iostream>

#include <opencv2/highgui/highgui.hpp>

#include <mynteyed/camera.h>
#include <mynteyed/utils.h>

MYNTEYE_USE_NAMESPACE


Camera cam;

cv::Mat getDepthImage(){
  auto image_depth = cam.GetStreamData(ImageType::IMAGE_DEPTH);
  if (image_depth.img) {
    std::cout << "Get Depth Image success" << std::endl << std::endl;
    // cv::Mat depth = image_depth.img->To(ImageFormat::DEPTH_BGR)->ToMat();
    // cv::imshow("depth", depth);
    auto depth_img = image_depth.img->To(ImageFormat::COLOR_BGR);
    cv::Mat depth(depth_img->height(), depth_img->width(), CV_8UC3,
        depth_img->data());
    return depth;
  }else{
    std::cout << "Get Depth Image failed" << std::endl << std::endl;
    cv::Mat m(1,1,CV_8UC3);
    return m;
  }
}



int init() {
  DeviceInfo dev_info;
  if (!util::select(cam, &dev_info)) {
    return 1;
  }
  util::print_stream_infos(cam, dev_info.index);

  std::cout << "Open device: " << dev_info.index << ", "
    << dev_info.name << std::endl << std::endl;

  OpenParams params(dev_info.index);
  params.dev_mode = DeviceMode::DEVICE_DEPTH;
  params.depth_mode = DepthMode::DEPTH_COLORFUL;
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

  // std::cout << "Press ESC/Q on Windows to terminate" << std::endl;

  // cv::namedWindow("depth");

  // auto image_depth = cam.GetStreamData(ImageType::IMAGE_DEPTH);
  // if (image_depth.img) {
  //   // cv::Mat depth = image_depth.img->To(ImageFormat::DEPTH_BGR)->ToMat();
  //   // cv::imshow("depth", depth);
  //   auto depth_img = image_depth.img->To(ImageFormat::COLOR_BGR);
  //   cv::Mat depth(depth_img->height(), depth_img->width(), CV_8UC3,
  //       depth_img->data());
  //   cv::imshow("depth", depth);
  // }

  // cv::waitKey(-1);

  // cam.Close();
  // cv::destroyAllWindows();
  return 0;
}

// int main(){
  // DeviceInfo dev_info;
  // if (!util::select(cam, &dev_info)) {
  //   return 1;
  // }
  // util::print_stream_infos(cam, dev_info.index);

  // std::cout << "Open device: " << dev_info.index << ", "
  //   << dev_info.name << std::endl << std::endl;

  // OpenParams params(dev_info.index);
  // params.depth_mode = DepthMode::DEPTH_COLORFUL;
  // params.stream_mode = StreamMode::STREAM_2560x720;
  // params.ir_intensity = 4;
  // params.framerate = 30;

  // cam.Open(params);

  // std::cout << std::endl;
  // if (!cam.IsOpened()) {
  //   std::cerr << "Error: Open camera failed" << std::endl;
  //   return 1;
  // }
  // std::cout << "Open device success" << std::endl << std::endl;

  // std::cout << "Press ESC/Q on Windows to terminate" << std::endl;

  // cv::namedWindow("depth");

  // auto image_depth = cam.GetStreamData(ImageType::IMAGE_DEPTH);
  // if (image_depth.img) {
  //   // cv::Mat depth = image_depth.img->To(ImageFormat::DEPTH_BGR)->ToMat();
  //   // cv::imshow("depth", depth);
  //   auto depth_img = image_depth.img->To(ImageFormat::COLOR_BGR);
  //   cv::Mat depth(depth_img->height(), depth_img->width(), CV_8UC3,
  //       depth_img->data());
  //   cv::imshow("depth", depth);
  // }

  // cv::waitKey(-1);

  // cam.Close();
  // cv::destroyAllWindows();
//   return 0;
// }

int main(){
  init();

  std::cout << "Press ESC/Q on Windows to terminate" << std::endl;
  

  cv::namedWindow("depth");
  cv::Mat depth = getDepthImage();
  cv::imshow("depth", depth);
  cv::waitKey(-1);

  cv::destroyAllWindows();
  cam.Close();
  return 0;
}