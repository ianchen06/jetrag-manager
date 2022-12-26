# Jetrag Manager

A simple web UI to manage Jetrag crawler jobs

## Getting Started

```
# Install Python dependancies
pip install -r requirements.txt

# Run the Flask app in development mode
flask --debug --app app run
```

### Example database schema
```
CREATE TABLE `item` (
  `id` varchar(17) NOT NULL, 
  `backcountry_id` varchar(20) NOT NULL, 
  `name` varchar(255) NOT NULL, 
  `url` varchar(512) NOT NULL, 
  `brand` varchar(50) NOT NULL, 
  `gender` varchar(10) NOT NULL, 
  `color` varchar(128) NOT NULL, 
  `edited` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, 
  PRIMARY KEY (`id`), 
  UNIQUE KEY `backcountry_id color unique constraint` (`backcountry_id`, `color`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8
```

### Example data in CSV format
```
id,backcountry_id,name,url,brand,gender,color,edited,created
00000fc6b65c94ad,IOS001B,Trapper II Pant - Toddlers',https://www.backcountry.com/isbjorn-of-sweden-trapper-ii-pant-toddlers,Isbjorn of Sweden,boys,Swedish Blue,2022-12-20 01:34:10,2022-11-29 13:38:09
000024346626b9c6,IMR000T,Lucky Charm Spray Skirt,https://www.backcountry.com/immersion-research-lucky-charm-spray-skirt,Immersion Research,unisex,Gray,2022-12-20 14:28:54,2022-11-29 13:31:40
00005055fb0cc491,BNGZ05G,Long-Sleeve Crewneck T-Shirt - Past Season - Women's,https://www.backcountry.com/basin-and-range-long-sleeve-crewneck-t-shirt-womens,Basin and Range,women,Gull Grey,2022-12-20 00:28:24,2022-11-29 11:03:52
00005d60c76c6c5f,RYW003V,Merino Wool Blend Sun Hoodie,https://www.backcountry.com/rep-your-water-merino-wool-blend-sun-hoodie,Rep Your Water,men,Grass,2022-12-20 15:48:39,2022-11-29 15:03:08
000082ffac5993f4,PATZ9LN,Los Gatos Fleece Jacket - Women's,https://www.backcountry.com/patagonia-los-gatos-fleece-jacket-womens,Patagonia,women,Pampas Tan,2022-12-20 13:47:21,2022-11-29 14:33:36
00021453bc217a7e,BAG00FU,Scout 2 Platinum Footprint,https://www.backcountry.com/big-agnes-scout-2-platinum-footprint,Big Agnes,unisex,Gray,2022-12-20 13:22:58,2022-11-29 11:22:22
0002517b27852cd3,DMMB013,Halfnut,https://www.backcountry.com/dmm-halfnut,DMM,unisex,Gold,2022-12-20 11:45:56,2022-12-06 14:13:28
00028e443d47cefd,MAQ0041,Training Jersey - Women's,https://www.backcountry.com/maap-training-jersey-womens,MAAP,women,Black,2022-12-20 09:12:24,2022-12-20 09:12:24
00038bf6238bcc97,MAMU5HG,Core T-Shirt - Men's,https://www.backcountry.com/mammut-core-t-shirt-mens,Mammut,men,Mello,2022-12-20 05:12:54,2022-11-29 13:48:00
```

## Resources

1. https://flask.palletsprojects.com/en/2.2.x/
1. https://getbootstrap.com