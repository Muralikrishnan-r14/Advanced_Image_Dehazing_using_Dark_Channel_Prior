# 🚗 Image Dehazing using Dark Channel Prior

🧩 Problem Statement

 Autonomous vehicles, drones, surveillance systems, and robotics heavily rely on computer vision for critical tasks like object detection, obstacle avoidance, lane recognition, and navigation. However, environmental conditions such as haze, fog, smoke, and mist significantly impair the clarity of visual data, making it challenging to detect objects and navigate accurately.
This problem becomes especially critical in complex terrains like hill stations with sharp curves, hairpin bends, and steep gradients, where precise object identification and road boundary detection are essential to avoid accidents. In such areas, vehicles and drones need to accurately detect pedestrians, road signs, oncoming traffic, and unexpected obstacles under poor visibility conditions caused by adverse weather.


🎯 Goals

The primary goal of this project is to restore image clarity in real time, thereby enhancing the performance of computer vision systems across multiple domains. This real-time dehazing solution aims to improve safety, reliability, and performance in challenging environments by ensuring:

1. Autonomous Vehicles: Safe driving through foggy hill stations, maintaining lane discipline, and avoiding obstacles on curves and bends.

2. Drones: Precision obstacle avoidance and tracking while navigating through low-visibility environments, such as mountain paths and forests.

3. Fire Rescue Operations: Efficiently identifying trapped individuals and hazards in smoke-filled areas to streamline rescue missions.

4. Surveillance Systems: Effective monitoring of activities and tracking objects in foggy or smoky conditions in both urban and remote environments.

5. Robotic Vision Systems: Accurate path planning and object manipulation in outdoor conditions affected by haze and mist.

By restoring visibility, this project enhances vision-based systems, facilitating better decision-making and operational efficiency in diverse applications.


 
 
📜 Overview

 This project implements real-time video dehazing using the Dark Channel Prior (DCP) algorithm. The method addresses the challenges of atmospheric scattering caused by haze, fog, or smog, which reduces image clarity and makes object detection difficult. By enhancing visibility, this solution improves the accuracy of downstream computer vision tasks like object detection and tracking.
This technology plays a crucial role in autonomous cars, drones, robotic vision systems, fire rescue missions, and surveillance systems, ensuring that operations remain safe and efficient in adverse weather conditions.

 🔧 Technical Details
The algorithm performs the following steps:

1. Dark Channel Computation:
Extracts the minimum intensity values within local patches to identify the "dark channel" of the input frame.

2. Atmospheric Light Estimation:
Identifies the brightest pixels in the dark channel to estimate the intensity of ambient light.

3. Transmission Map Calculation:
Computes the transmission map to model the amount of light penetrating the haze.

4. Dehazing Equation Application:
Restores the clear image using a pixel-wise operation, ensuring accurate color restoration and brightness adjustment.

5. Real-time Display:
Streams the original and dehazed frames side by side for live comparison.

📈 Performance Optimization and 📊 Results

Performance optimization strategies include efficient memory handling and real-time processing at approximately 30 FPS, ensuring swift responsiveness in dynamic environments.
The deployment of the Dark Channel Prior (DCP) algorithm has yielded transformative results in enhancing image clarity in adverse weather conditions. Through rigorous testing, this technology has proven instrumental across several high-stakes domains:

1. Autonomous Vehicles: By significantly improving object detection capabilities, this technology enables safer navigation through foggy terrains and sharp curves, reducing accident rates and enhancing passenger safety.

2. Drones: Enhanced visibility allows drones to conduct precision operations in low-visibility environments, such as disaster zones or densely forested areas, facilitating effective monitoring and intervention.

3. Robotic Vision Systems: The improved clarity assists robots in accurately interpreting their surroundings, thus enhancing their operational efficiency in tasks ranging from industrial automation to search and rescue missions.

4. Fire Rescue Missions: The ability to penetrate smoke and haze enables first responders to locate trapped individuals and assess hazardous situations more effectively, ultimately saving lives.

5. Surveillance Systems: Enhanced image quality in challenging conditions allows for more reliable monitoring and tracking, contributing to increased security in urban and rural settings.

This technology not only enhances performance but also revolutionizes decision-making processes in environments previously hindered by poor visibility. By ensuring clear visual data, the DCP algorithm significantly elevates the operational capabilities of vision-based systems, paving the way for innovative applications and improved safety measures across various industries.

The results underscore the profound impact of advanced dehazing techniques in shaping the future of autonomous and intelligent systems, demonstrating their crucial role in enhancing both safety and efficiency.










