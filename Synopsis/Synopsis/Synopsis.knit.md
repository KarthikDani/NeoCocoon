---
title: "Neo Cocoon: Low-cost and Portable Neonatal Protection and Development System"
authors:
  - name: Karthik M Dani
    department: Dept of Medical Electronics Engineering
    affiliation: B.M.S College of Engineering
    location: Bangalore - 560019
    email: karthik.ml22@bmsce.ac.in
    
  - name: Sanjana WG
    department: Dept of Medical Electronics Engineering
    affiliation: B.M.S College of Engineering
    location: Bangalore - 560019
    email: sanjana.ml22@bmsce.ac.in
    
  - name: Darshan S K
    department: Dept of Medical Electronics Engineering
    affiliation: B.M.S College of Engineering
    location: Bangalore - 560019
    email: darshan.ml22@bmsce.ac.in
    
  - name: Dr. H. N. Suma
    department: Dean Innovation
    affiliation: B.M.S College of Engineering
    location: Bangalore - 560019
    email: hns.ml@bmsce.ac.in
  
  - name: Mr. Balaji Raghavendra S
    department: Founder and CEO
    affiliation: Piroya Technologies
    location: Bangalore - 560019
    email: balaji.s@piroya.com
    
    
abstract: |
  This project addresses the critical issue of neonatal care by aiming to develop an affordable medical device, particularly focusing on the high rates of morbidity and mortality among preterm infants. In 2020, approximately 13.4 million premature births occurred globally, with a significant number resulting in complications that lead to infant mortality, particularly in low-income countries. By leveraging non-invasive technologies for monitoring vitals of neonates, this project aims to enhance the detection and management of neonatal jaundice and hypothermia—two prevalent conditions affecting newborns.
  
  The study utilizes a combination of non contact infrared thermometry, phototherapy techniques, Internet of Medical Things (IoMT) and efficient RDMS, from monitoring body temperature, detecting and treating jaundice, sharing it to the device hosted webserver for ease of use and access. The effectiveness of these interventions will be evaluated through a systematic workflow that integrates data collection, processing, and real-time monitoring. Additionally, the project emphasizes the importance of immediate postnatal care practices, such as drying and wrapping newborns, to mitigate hypothermia risk and improve thermal protection. 
  
  Through this multidisciplinary approach, the project aspires to develop cost-effective solutions that can be implemented in resource-limited settings, thereby reducing neonatal mortality rates. The anticipated outcomes include improved clinical practices and increased accessibility to essential neonatal care technologies, ultimately contributing to better health outcomes for vulnerable population.
  
keywords:
  - NICU
  - Medical Device
  - IoMT
  - AI
  - Neonatal Protection
  - Portable
  - Monitoring
  - Premature Infants
  - Temperature
  - SpO2
  - Heart Rate
  - ECG
  - Phototherapy
  - Data Logging
  - User-Friendly Interface
  - Microprocessor
  - Microcontroller
  - Healthcare
  - Jaundice Treatment
  
bibliography: /home/karthik/NeoCocoon/Synopsis/Neococoon Zotero Export Literature/Neococoon Zotero Export Literature.bib
biblio-style: unsrt
output: rticles::arxiv_article
csl: ieee.csl
#nocite: '@*'
---

# Introduction

Babies born before the completion of 37 weeks of pregnancy are classified as premature @noauthor_thermal_nodate. They are further categorized as follows:

1.  **Extremely premature:** Less than 28 weeks

2.  **Very premature:** 28 to 32 weeks

3.  **Moderate to late premature:** 32 to 37 weeks

## Background

### Low Birth Weight (LBW) as consequence of Pre Mature Birth

**Low Birth Weight (LBW)** refers to infants born weighing less than 5 pounds, 8 ounces (2,500 grams). In contrast, the average newborn typically weighs around 8 pounds. Much of a baby's weight is accumulated in the final weeks of pregnancy, so being born prematurely often results in low birth weight @noauthor_low_nodate.

Another cause of Low Birth weight is condition called **Intrauterine Growth Restriction (IUGR)** arises when a baby does not grow adequately during pregnancy.

#### Health Complications of Low Birth Weight

Infants with low birth weight encounter numerous health complications that can adversely affect their growth and development. One of the significant issues they face is reduced oxygen levels at birth, which may lead to immediate respiratory difficulties. These infants often struggle to maintain a stable body temperature, putting them at risk for hypothermia. Additionally, many experience feeding challenges, as their ability to suck may be compromised, resulting in inadequate weight gain. Their underdeveloped immune systems make them more susceptible to infections. Furthermore, low birth weight can lead to breathing issues like infant respiratory distress syndrome, stemming from immature lung development. Neurological problems may also arise, such as intraventricular hemorrhage, which involves bleeding within the brain. The risk of digestive complications, particularly necrotizing enterocolitis, poses further concerns. Lastly, there is an elevated risk of sudden infant death syndrome (SIDS) during the early months of life, adding to the vulnerabilities faced by these infants. @noauthor_low_nodate

#### 3 methods to address Low Birth Weight as a Medical Electronics Engineer

Management for LBW often involves:

1.  Care in a neonatal intensive care unit (NICU).

2.  Temperature-controlled environments such as a warmer or an infant incubator.

3.  Specialized feeding methods, including tube feeding for infants unable to suck, or intravenous (IV) feeding.

While we choose the 2nd method to address the problem, we choose innovation in domain of incubators instead of warmers for the reasons listed in the latter sections.

# Motivation

## Pre Mature Birth Statistics

In 2020, 10% of all births worldwide, equating to approximately 13.4 million, were premature. In 2019, around 900,000 children died due to complications arising from preterm birth. In low-income countries, nearly half of the infants born at or before 32 weeks gestation (i.e., two months premature) do not survive due to a lack of effective and affordable care @noauthor_thermal_nodate @noauthor_nacimientos_nodate. See figure \ref{fig:fig1}

Furthermore, more than 90% of extremely preterm infants (born before 28 weeks) in low-income settings die within the first few days of life, in stark contrast to less than 10% in high-income countries. It is estimated that three-quarters of these deaths could be averted with existing, cost-effective interventions. The rate of premature births in 2020 varied from 4% to 16% @noauthor_nacimientos_nodate.

\begin{figure}
  \centering
  \includegraphics[width=350pt,height=200pt]{images/clipboard-1098342472.png} % Adjust the path to your image
  \caption{Global statistics on premature births in 2020, highlighting the prevalence of preterm births and associated mortality rates, particularly in low-income countries.}
  \label{fig:fig1}
\end{figure}

In 2022, nearly half (47%) of all deaths among children under five years old took place during the neonatal period, which refers to the first 28 days of life. Every day, approximately 6,500 newborns die, primarily due to inadequate quality of care at birth. Most neonatal deaths (about 75%) occur within the first week of life, highlighting the urgent need for effective interventions during this crucial timeframe. @noauthor_mortalidad_nodate See figure \ref{fig:fig2}

\begin{figure}
  \centering
  \includegraphics[width=350pt,height=200pt]{images/clipboard-3806704517.png} % Adjust the path to your image
  \caption{Nearly 47\% of child deaths under five occur in the neonatal period, underscoring the need for timely interventions.}
  \label{fig:fig2}
\end{figure}

Therefore the health outcomes for premature newborns in remote and resource-limited areas stems from the critical need to address the vulnerabilities these infants face. Premature babies are at a higher risk of complications due to their underdeveloped physiological systems. In regions where access to medical facilities and skilled healthcare providers is limited, traditional neonatal care may not be feasible. Thus, developing solutions that are smarter, safer, and responsive to the unique challenges of these environments is essential. These solutions should be designed to be user-friendly, minimizing the need for extensive training and allowing caregivers to provide effective support with limited resources. By focusing on reducing dependency on human supervision, we can create reliable systems that ensure consistent care for these vulnerable infants, ultimately aiming to improve their survival rates and long-term health outcomes.

# Literature Survey

WHo claims Hypothermia is a significant contributor to neonatal illness and death, particularly among low birth weight and normal newborns. To combat this, thermal protection measures are crucial for maintaining a normal body temperature of 36.5–37.5°C after birth, as newborns are often exposed to cooler environments that cause rapid heat loss. @noauthor_thermal_nodate

$$
SizeOfInfant \propto T_{OutsideNormal}
$$

Where, $T_{OutsideNormal}$ is the Temperature outside the normal range.

This heat loss can occur through various mechanisms, including evaporation, conduction, convection, and radiation, and can result in significant temperature drops within the first 10-20 minutes post-delivery. It's important to maintain a delivery room temperature between 25–28°C, with a maximum tolerable temperature of around 35°C for naked newborns. Separating newborns from their mothers complicates thermal protection efforts and increases the risk of infections; thus, immediate drying and wrapping of newborns are essential practices. Hypothermia can be classified into three categories: mild (36–36.4°C), moderate (32–35.9°C), and severe (\<32°C), with prolonged exposure leading to impaired growth and increased mortality rates. See figure \ref{fig:fig3}

\begin{figure}
  \centering
  \includegraphics[width=350pt,height=200pt]{images/clipboard-2554530258.png} % Adjust the path to your image
  \caption{Effective thermal protection for newborns is crucial, as hypothermia can occur rapidly post-delivery.}
  \label{fig:fig3}
\end{figure}

Effective management includes assessing for infections and implementing safe heating practices to avoid burns. Conversely, hyperthermia, defined as a body temperature exceeding 37.5°C, can result in dehydration and necessitates quick evaluation for infections. Guidelines for incubator use specify maintaining an air temperature of 35–36°C, conducting regular temperature checks, ensuring cleanliness, and encouraging skin-to-skin contact between newborns and their mothers. @noauthor_thermal_nodate

The MQTT protocol has been evaluated in both the biomedical engineering laboratory and the hospital's neonatology unit. Premature infants often lack sufficient body fat and organ development to maintain their body temperature, which should be kept between 28°C and 34°C. Reducing access time to newborns is vital to minimize heat and oxygen loss. @aya-parra_monitoring_2023

The BreathAnalyzer, a smartwatch that uses an AI model based on decision trees, improves accuracy in detecting respiratory sinus arrhythmia (RSA) from 35.37% to 80%, achieving an average of 42% accuracy across various scenarios. Calibration tests were conducted in accordance with the ISO/IEC 1725:2017 standard to ensure measurement reliability. Despite advancements, there are no existing devices that fully meet the needs of the medical field. The Internet of Things in medicine (IoMT) is essential for developing comprehensive technological solutions. However, a progressive web application (SiMCa-Bio) was created to monitor incubator conditions in real-time, focusing only on temperature, humidity, and sound, with a sampling frequency of 5 minutes and data transmission every 10 minutes @aya-parra_monitoring_2023. Hoever Elevated levels of relative humidity are not advisable for infants, as they can encourage the growth of bacteria and germs @pujiastuti_analysis_2022

The transition from traditional monitoring methods to wearable devices focuses on reducing adhesive-related skin injuries. This approach promotes the use of soft, flexible materials and gentler adhesion techniques while emphasizing the design of all-in-one devices. The priority is on non-invasive monitoring solutions that enhance accessibility, particularly for high-risk patients, such as those born prematurely (with a gestational age of less than 37 weeks) or with low birth weight (typically less than 2.5 kg) @zhou_skin-interfacing_2024

Smart infant incubator monitoring and control system that utilizes a gas sensor, accelerometer, and Peltier module, which are not part of our current design was developed by K C N Raju @k_c_n_smart_2024. The system automatically adjusts the Peltier module and humidifier when temperatures exceed 36°C to 37.2°C and humidity exceeds 60%, ensuring an optimal environment for premature and critically ill newborns.

A major challenge identified is the imbalance between caregivers and patients, leading to increased workloads and compromised monitoring of incubators. The study emphasizes maintaining temperatures between 36°C and 37.5°C, with a targeted rectal temperature of around 36°C, and humidity levels between 40% and 60%. Additionally, the integration of artificial intelligence and live monitoring through cameras enhances the care provided. However, limitations include the use of an Arduino Wi-Fi R3 and reliance on an LCD display and ThingSpeak for IoT applications.

Another study @ningsih_monitoring_2023 focuses on an IoT-based baby incubator monitoring system utilizing Raspberry Pi Zero W. It monitors critical environmental parameters, including temperature, humidity, and oxygen levels, in real-time to safeguard infants in incubators. The system is connected to a central computer for data visualization, alarms, and alerts, enabling healthcare professionals to monitor the situation remotely. The incubator is maintained at a temperature range of 32 to 36 degrees Celsius to ensure the baby's skin remains at a healthy temperature of 37 degrees Celsius. Additionally, appropriate humidity levels warm the baby's breath and facilitate the entry of moist air into the lungs.

Adding on to it, @bogdan_sciendo_2016 emphasized that heating systems require careful management, particularly during the winter months, to maintain a consistent temperature for optimal comfort. Humidity levels in solids and liquids are measured using hygrometers. Various methods for measuring moisture include assessing changes in resistivity, variations in capacitance, or monitoring the attenuation of microwaves.

This literature @bogdan_sciendo_2016 provided information regarding checksum @maxino_effectiveness_2009 for a typical DHT22 sensor that was in communication via I2C protocol:

$$ 
Data Structure = 8 bits (RH_{int}) + 8 bits (RH_{dec}) + 8 bits (T_{int}) + 8 bits (T_{dec}) + 8 Checksum Bits 
$$

Where, $RH_{int}$ = Integer Relative Humidity, $RH_{dec}$ = Decimal Relative Humidity, $T_{int}$ = Integer Temperature and $T_{dec}$ = Decimal Temperature.

Around 75,000 children worldwide suffer from brain dysfunction due to jaundice, with neonatal hyperbilirubinemia causing approximately 114,100 preventable deaths and many long-term disabilities. Transcutaneous Bilirubin (TcB) is a non-invasive method for jaundice detection, with its phototherapy roots tracing back to England, where sunlight exposure was linked to reduced jaundice in infants. Bilirubin absorbs light predominantly in the blue spectrum near 460 nm, triggering photochemical reactions in the skin. The most effective treatment involves light in the 460 to 490 nm range. In this study, a camera was set 30 cm from the subject at a 45-degree angle under 200 lux ambient lighting, using color transformation and Otsu thresholding for skin detection. @hashim_neonatal_2021

A limitation of this approach is the dependence on MATLAB, a commercial software, which lacks on-device detection capabilities.

The study examines neonatal hyperbilirubinemia and Rhesus disease, focusing on their incidence and impacts in 2010. It highlights the critical importance of early detection and effective management to prevent severe outcomes, such as neurological damage and mortality. The authors urge health systems to prioritize these strategies to reduce morbidity and mortality rates. Key takeaways include the necessity of early detection, the potential of treatment protocols to mitigate long-term impairments, and the benefits of incorporating screening methods to enhance neonatal health outcomes. @bhutani_neonatal_2013

# Objectives

## Primary Objectives

1.  **Affordablity**: Develop a low-cost yet cutting-edge device that enhances healthcare delivery in resource-limited settings, ensuring accessibility for all.

2.  **Real-Time Monitoring of Essential Health Metrics**: Implement continuous monitoring capabilities for vital health parameters that includes body temperature @wibawa_design_2022, ambient temperature, ambient humidity levels, neonatal heart rate, blood oxygen saturation ($SpO_2$) and Electrocardiogram (ECG).

3.  **User-Friendly Touch Screen Interface**: Design an intuitive touch-screen user interface that simplifies interaction with the device.

4.  **Comprehensive Data Logging**: Facilitate automatic logging of health data over time, enabling caregivers to track trends and make informed decisions regarding the care of premature newborns.

5.  **Remote Data Accessibility via IoT**: Enable remote access to device data through IoT integration, allowing healthcare professionals to monitor patients’ conditions from distant locations, enhancing collaboration and response times.

6.  **Critical Alarm System**: Integrate a robust alarm system that alerts caregivers to critical changes in health parameters, ensuring prompt action can be taken in emergencies.

7.  **Phototherapy Capabilities**: Include a phototherapy function for the treatment of neonatal jaundice, utilizing advanced light therapy to support the health and recovery of affected infants.

## Secondary Objectives

1.  **AI-Driven Jaundice Detection and Classification**: Explore the potential for AI integration to enhance jaundice detection and classification @hashim_neonatal_2021 based on Kramer's rule. Availability of data is the major problem to implement this. A potential dataset @abdulrazzak_njn_2023 was found that can help us meet this objective.

2.  **Produce Instantaneous Reports**: Create a reporting function that generates up-to-date health status reports, enabling healthcare professionals to swiftly evaluate the condition of premature infants without the need for manual data input.

3.  **Compliance and Record Keeping**: Establish automated reporting that aligns with healthcare standards and regulations, simplifying the record-keeping process for neonatal care and ensuring accessibility for audits and assessments.

# Materials and Methods

## Materials

### Software requirements

Software used is listed in the table \ref{tab:table1}

\begin{table}[h]
    \centering
    \caption{Software Requirements for Project}
    \begin{tabular}{@{}lll p{1cm} p{4cm}@{}}
        \toprule
        \textbf{Software} & \textbf{Inventor/Developer} & \textbf{Open Source / Paid} & \textbf{Version} & \textbf{Purpose} \\
        \midrule
        KiCAD & Jean-Pierre Charras & Open Source & 7.0.0 & Schematic and PCB design \\
        Python & Python Software Foundation & Open Source & 3.12.0 & Programming \\
        Thonny & Aivar Annamaa & Open Source & 4.1.1 & Microcontroller firmware \\
        Visual Studio Code & Microsoft & Open Source & 1.82.0 & Code editing, debugging \\
        Node RED & JS Foundation (IBM) & Open Source & 3.1.0 & IoT workflows automation \\
        Grafana & Grafana Labs & Open Source & 10.1.1 & Data visualization \\
        Influx DB & InfluxData & Open Source & 2.7.0 & Time-series database \\
        HTML, CSS, JavaScript & Various & Open Source & - & Web Development \\
        PyQt5 & Riverbank Computing & Open Source (GPL) & 5.15.9 & On Device GUI \\
        MySQL & Oracle Corporation & Open Source (GPL) & 8.1.0 & DBMS \\
        \bottomrule
    \end{tabular}
    \label{tab:table1}
\end{table}

### Hardware requirements

Refer Table \ref{tab:table2} given below for hardware components used in the project.

\begin{table}[h]
    \centering
    \caption{Hardware Requirements}
    \begin{tabular}{@{}lllp{2cm}@{}}
        \toprule
        \textbf{Item No.} & \textbf{Part Description} & \textbf{Specs} & \textbf{Quantity} \\
        \midrule
        1 & Non Contact Temperature Sensor & MLX90614 ESF & 1 \\
        2 & Temperature and Relative Humidity Sensor & GY-SHT40 & 1 \\
        3 & SpO2 and Heart Rate Sensor & MAX30102 & 1 \\
        4 & Sound Sensor & MAX9814 & 1 \\
        5 & ECG Module + Cables + Electrodes & AD8232 & 1 \\
        6 & Microcontroller board & RP2350 Pico 2 board & 1 \\
        7 & Ambient Light sensor for Phototherapy Unit & VEML6030 & 1 \\
        8 & ECG Gel Electrodes & 3 each in 5 Packs & 2 \\
        9 & Raspberry Pi Memory Card & Raspberry Pi Official 32GB V3.0, A2 Class & 1 \\
        10 & Raspberry Pi Microprocessor Board & Raspberry Pi 5 Model B 8GB RAM & 1 \\
        11 & Active Cooler for Microprocessor Board & - & 1 \\
        12 & Raspberry Pi Power Supply & 27W USB-C PD Power Supply & 1 \\
        13 & IO Expansion Hat for RPI 5 & - & 1 \\
        14 & Micro HDMI to HDMI Cable & Official RPi 5 Micro HDMI to HDMI & 1 \\
        15 & SpO2 Probe & - & 1 \\
        16 & RS232 to USB Adapter for SpO2 Probe & - & 1 \\
        17 & ASAIR AO-08 Medical Oxygen Sensor & ASAIR AO-08 & 1 \\
        18 & RPI Camera Module 3 NoIR – Wide & Sony IMX706 & 1 \\
        19 & Ultrasonic Humidifier & - & 1 \\
        20 & PTC Heating element & - & 1 \\
        \bottomrule
    \end{tabular}
    \label{tab:table2}
\end{table}

## Methods

Tentative workflow for the project is given in figure \ref{fig:fig4}

\begin{figure}
  \centering
  \includegraphics[width=500pt,height=500pt]{images/clipboard-1005866267.png} % Adjust the path to your image
  \caption{Key stages and processes involved in developing the project. `}
  \label{fig:fig4}
\end{figure}

### Why does this methodology work?

The workflow method applied in this project from PCB design to data visualization. Each stage is interconnected, promoting efficient data processing and communication between devices.

1.  **PCB Design:** The use of KiCAD @noauthor_kicad_nodate for PCB design allows for precise generation of schematics and layouts. This structured approach ensures that the hardware is optimally configured for subsequent processes. @noauthor_kicad_nodate-1. See figure \ref{fig:fig5} for schematic and figure \ref{fig:fig6} for layout design

\begin{figure}
  \centering
  \includegraphics[width=300pt,height=250pt]{images/schematic.jpeg} % Adjust the path to your image
  \caption{Schematic containing circuits seperated as different sections for enhancing readability.}
  \label{fig:fig5}
\end{figure}


\begin{figure}
  \centering
  \includegraphics[width=300pt,height=280pt]{images/pcb.png} % Adjust the path to your image
  \caption{PCB incorporating power delivery, communication, connectors, microcontroller reset button and power noise filter.}
  \label{fig:fig6}
\end{figure}

2.  **Microcontroller Programming:** The workflow effectively leverages the capabilities of the Raspberry Pi Pico 2 through MicroPython, programmed using Thonny. This combination allows for direct hardware manipulation, essential for handling sensor data collection accurately. The I2C and Analog interfaces used for data transmission enable effective communication between the sensors and the microcontroller.

3.  **Microprocessor Programming:** Implementing Python 3.12 on the Raspberry Pi 5 facilitates a robust programming environment for developing the device's user interface (See figure \ref{fig:fig7} and figure \ref{fig:fig8}). Python’s extensive libraries simplify complex programming tasks, making it an ideal choice for creating responsive and interactive applications.

4.  **Data Transmission Protocols:** Sensor data is communicated through I2C and Analog. The transmission of raw data from the Raspberry Pi Pico 2 to the Raspberry Pi 5 via UART ensures that data is transferred swiftly and reliably.

5.  **IoT Integration:** The integration of Node-RED, InfluxDB, and Grafana into the workflow enhances the Internet of Things (IoT) capabilities of the project. Node-RED facilitates flow-based programming, allowing users to design workflows visually, while InfluxDB stores time-series data efficiently. Grafana then visualizes this data, providing insightful dashboards for users to monitor and analyze system performance.

6.  **Database Management:** Utilizing MySQL for database management @noauthor_mysql_nodate establishes a reliable repository for storing device data. This approach to data organization ensures that information can be retrieved quickly.

\begin{figure}
  \centering
  \includegraphics[width=450pt,height=280pt]{images/ui1.png} % Adjust the path to your image
  \caption{Touch screen based Main Graphical user Interface shwowing vital health parameters for quick look and easy interaction.}
  \label{fig:fig7}
\end{figure}

\begin{figure}
  \centering
  \includegraphics[width=450pt,height=260pt]{images/ui2.png} % Adjust the path to your image
  \caption{GUI based History access for more insights during realtime monitoring.}
  \label{fig:fig8}
\end{figure}


#### Paying attention to Non Contact Infrared Temperature (NCIT) Measurement

This study @long_sciendo_2016 focuses on utilizing an infrared human body temperature sensor to convert the body's infrared radiation into a voltage signal. Experimental results indicate a temperature measurement error of less than 0.2°C, with a measurement time of approximately 4 seconds using a non-contact infrared thermometer. In contrast, mercury thermometers require direct contact and can take 5 to 10 minutes to measure temperature, often leading to inaccuracies due to external light interference.

The principle of infrared temperature measurement is based on the emission of electromagnetic waves from objects with temperatures above absolute zero, with the intensity of radiation depending on the object’s absolute temperature. Notably, all real objects, including the human body, have Beta values less than 1.0, and the main infrared radiation wavelength of the human body ranges from 9 to 10 um. This wavelength is not absorbed by air, allowing for accurate surface temperature determination based on infrared energy. @long_sciendo_2016

This literature @zhao_non-contact_2023 critically examines the performance of non-contact infrared thermometers (NCITs) and infrared thermometers (IRT) in monitoring body temperature, synthesizing data from 72 unique settings across 32 studies. Both NCITs and IRTs showed a positive correlation with traditional contact-based temperature measurement tools; however, NCITs exhibited slightly greater accuracy. Specifically, 29 out of 50 settings from NCIT studies and 4 out of 22 settings from IRT studies achieved accuracy levels within ±0.3°C. This suggests that while both types of thermometers are effective, NCITs may be the preferable option for more precise temperature monitoring.

#### Do NCITs have edge over traditional contact based temperature measurement?

Traditional methods of measuring body temperature often involve affixing sensors directly to the skin, which can compromise measurement accuracy due to environmental disturbances. A review that included 21 studies revealed that the bias in temperature readings can vary widely; some setups demonstrated minor discrepancies of less than 0.5°C, while others exhibited significant errors exceeding 0.5°C. These findings highlight the considerable influence that setup variables have on the accuracy of contact-based temperature sensors. Therefore, consistent documentation of these variables across studies is essential for accurate interpretation and reliable comparisons among different research findings. @macrae_skin_2018

#### Deciding between Resistive and Capacitive Touch Screen technologies in healthcare setting

\begin{table}[h]
    \centering
    \caption{Comparison of Resistive and Capacitive Touchscreens}
    \begin{tabular}{@{}lll@{}}
        \toprule
        Feature                  & Resistive Touchscreen                      & Capacitive Touchscreen                     \\ \midrule
        Structure                & Multiple layers with a conductive gap      & Single insulating layer with conductive film \\ 
        Interaction Method       & Detects pressure                           & Detects change in electric field           \\
        Input Types              & Any touch (conductive or non-conductive)  & Only conductive touch (e.g., human finger)  \\
        Accuracy                 & Moderate                                  & High                                      \\
        Response Time            & Slower                                    & Faster                                    \\ 
        Applications             & Versatile (various objects)               & Preferred for precise touch input          \\ \bottomrule
    \end{tabular}
\end{table}

While resistive touchscreens can register touch from various objects, capacitive touchscreens are more efficient and responsive, making them a preferred choice for applications requiring precise touch input, hence we choose this technology.

# Expected Outcomes

-   **Improved Public Health Monitoring**

    The development of a non-contact infrared temperature measurement system will enhance early detection of fever, a common indicator of infection, allowing for timely intervention and reducing the spread of infectious diseases.

-   **Accessibility and Convenience**

    The non-invasive nature of the device makes it suitable for use in diverse settings, including homes, schools, and healthcare facilities, thereby increasing accessibility to health monitoring tools, particularly in resource-limited environments. Reduction of

-   **Healthcare Costs**

    By facilitating early detection and monitoring of health conditions, the technology can potentially lower healthcare costs associated with hospital visits and treatments for advanced-stage illnesses.

-   **Enhanced Safety in Healthcare Settings**

    The ability to measure temperature without physical contact reduces the risk of cross-contamination, thus enhancing safety protocols in hospitals and clinics, especially in the context of infectious disease outbreaks.

-   **Support for Pediatric Care**

    The technology is particularly beneficial for monitoring infants and young children, providing parents and caregivers with a safe and efficient method for tracking body temperature without causing discomfort.

-   **Contribution to Research and Development**

    The insights gained from the implementation and performance evaluation of the system can contribute to the broader field of biomedical engineering and health technology research, fostering innovation and encouraging further advancements.

-   **Potential for Integration with Smart Health Systems**

    The device can be integrated into existing health monitoring systems and IoT platforms, paving the way for advanced health analytics and real-time data sharing, which can enhance public health responses during emergencies.

# Grants

We would like to extend my sincere gratitude to the **MSME Government of India** for their generous funding and support for this project. Their commitment to fostering innovation and entrepreneurship has been instrumental in making this initiative possible.

# Acknowledgement

We would like to express our gratitude and sincere thanks to our internal guide Dr. H N Suma and external guide Mr. Balaji Raghavendra S for giving us the opportunity and providing complete guidance throughout our project. Secondly, we would like to thank all the faculty members of our department for being a supportive part in our learning process. Further we would also like to thank our team members whose guidance, encouragement and suggestions have contributed immensely to the evolution of better ideas and completion of the project.

\newpage

# PO Attainment

\begin{table}[ht]
    \centering
    \caption{Program Outcomes (PO) and Program Specific Outcomes (PSO)}
    \begin{tabular}{@{}ll@{}}
        \toprule
        \textbf{Outcome Code} & \textbf{Description} \\ \midrule
        PO1  & \begin{minipage}[t]{10cm} \textbf{Engineering Knowledge:} Utilized engineering principles to design the hardware components neccessary and know-how of software aspects of the projet. Plan is done to implement the designs. \end{minipage} \\
        PO2  & \begin{minipage}[t]{10cm} \textbf{Problem Analysis:} Identified challenges in care of pre mature newborns, risks and consequences associated with it. \end{minipage} \\
        PO3  & \begin{minipage}[t]{10cm} \textbf{Design/Development of Solutions:} Ongoing design for an innovative temperature monitoring system that incorporates advanced sensing technologies and reliable communication protocols. \end{minipage} \\
        PO4  & \begin{minipage}[t]{10cm} \textbf{Conduct Investigation of Complex Problems:} Conducted thorough investigations into the effectiveness of different sensor technologies with acceptable error margins for healthcare settings. \end{minipage} \\
        PO5  & \begin{minipage}[t]{10cm} \textbf{Modern Tool Usage:} Leveraged modern tools like KiCAD for PCB design, Python and IoT for software development in conjuction with hardware. \end{minipage} \\
        PO6  & \begin{minipage}[t]{10cm} \textbf{Engineer and Society:} Developing a solution that addresses neonatal health issues, contributing positively to society. \end{minipage} \\
        PO7  & \begin{minipage}[t]{10cm} \textbf{Environment and Sustainability:} Ensured the design is energy-efficient and minimizes waste in manufacturing processes. \end{minipage} \\
        PO8  & \begin{minipage}[t]{10cm} \textbf{Ethics:} Adhered to ethical guidelines in medical device development, prioritizing patient safety and listed out medical standards neccessary to be met. \end{minipage} \\
        PO9  & \begin{minipage}[t]{10cm} \textbf{Individual and Teamwork:} Collaborated with team to achieve project goals while also managing individual tasks. \end{minipage} \\
        PO10 & \begin{minipage}[t]{10cm} \textbf{Communication:} Effectively communicated complex concepts and findings to MSME Govt of India when they had visited for signing funds in both technical and non-technical aspects. \end{minipage} \\
        PO11 & \begin{minipage}[t]{10cm} \textbf{Project Management:} Managing project timelines and resources efficiently, ensuring successful delivery of project milestones. \end{minipage} \\
        PO12 & \begin{minipage}[t]{10cm} \textbf{Life-Long Learning:} Engaged in continuous learning to stay updated with emerging technologies in biomedical engineering. \end{minipage} \\ \midrule
        PSO1 & \begin{minipage}[t]{10cm}\textbf{ Investigate, Implement, and Demonstrate biomedical systems:} To be done in the upcoming weeks \end{minipage} \\
        PSO2 & \begin{minipage}[t]{10cm} \textbf{Specify, Architect, and Prototype healthcare solutions:} Prototyping a healthcare solution that utilizes new technolgies such as infrared technology for non-contact temperature measurement. \end{minipage} \\
        PSO3 & \begin{minipage}[t]{10cm} \textbf{Design, Develop, and Verify algorithms for medical purposes:} Developing algorithms for accurate temperature detection and verification using sensor data. \end{minipage} \\ \bottomrule
    \end{tabular}
    \label{tab:outcomes}
\end{table}

# References
