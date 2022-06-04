{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "202255122-김지훈_결과물",
      "provenance": [],
      "authorship_tag": "ABX9TyNv3s1hHbT0KSnThGgVdjRZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jkim2397/week12homework/blob/jkim2397-sel2/202255122_%EA%B9%80%EC%A7%80%ED%9B%88_%EA%B2%B0%EA%B3%BC%EB%AC%BC.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zbR5E7UyHemd"
      },
      "outputs": [],
      "source": [
        "import selectors\n",
        "from selenium import webdriver\n",
        "from selenium.webdriver.common.by import By \n",
        "from selenium.webdriver.common.keys import Keys\n",
        "import time\n",
        "import csv\n",
        "\n",
        "driver = webdriver.Chrome(executable_path=\"C:/Python 3.10/chromedriver_win32/chromedriver.exe\")\n",
        "browser = webdriver.Chrome('C:/Python 3.10/chromedriver_win32/chromedriver.exe')   \n",
        "browser.get('https://www.naver.com')\n",
        "browser.implicitly_wait(10)\n",
        "browser.find_element_by_css_selector('a.nav.shop').click()\n",
        "time.sleep(2)\n",
        "search = browser.find_element_by_css_selector('input._searchInput_search_input_QXUFf')\n",
        "search.click()\n",
        "search.send_keys('아이폰 13')\n",
        "search.send_keys(Keys.ENTER)\n",
        "\n",
        "before_h=browser.execute_script(\"return window.scrollY\")\n",
        "while True:\n",
        "    browser.find_element_by_css_selector(\"body\").send_keys(Keys.END)\n",
        "    time.sleep(10)\n",
        "    after_h = browser.execute_script(\"return window.scrollY\")\n",
        "    if after_h == before_h:\n",
        "        break\n",
        "    before_h == after_h\n",
        "f = open(r\"C:/Users/82102/Desktop/asdf/03_크로울링/data.csv\", 'w', encoding='CP949', newline='')\n",
        "csvWriter = csv.writer(f)\n",
        "\n",
        "\n",
        "items = browser.find_element(\".basicList_info_area__17Xyo\")\n",
        "for item in items:\n",
        "    name = item.find_element_By.CSS_SELETOR(\".basicList_title__3P9Q7\").text\n",
        "    try:\n",
        "        price = item.find_element_By_CSS_SELECTOR(\".basicList_price_area__1UXXR\").text\n",
        "    except:\n",
        "        price = \"판매중단\"\n",
        "    link = item.find_element_By_CSS_SELECTOR(\".basicList_title__3P9Q7 > a\").get_attribute('href')\n",
        "    print(name, price, link)\n",
        "    csvWriter.writerow([name, price, link])\n",
        "\n",
        "f.close()"
      ]
    }
  ]
}