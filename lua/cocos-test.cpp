auto clipper = ClippingNode::create()
auto stencil = Sprite::craete("sample.png")

//auto clipper = ClippingNode::create(stencil)

clipper->setStencil(stencil)
clipper->setInverted(false)
clipper->setAlphaThreshold(0)


//structure
auto sp = Sprite::create()
std::shared_ptr<Vector<Sprite *>> vec0 = std::make_shared<Vector<Sprite *>>();
vec0->pushBack(sp)
Vector<Sprite *> vec1(5);
vec1.insert(0,sp)

vec1.pushBack(vec0)
for(auto sp : vec1){

}

Vector<Sprite *> vec2(* vec0)
if (vec0->equals(vec2)){

}


//map
typedef std::unorderd_map(k,v) RedMap;
RefMap _data;

SimpleAudioEngine::getInstance()->preloadBackgroundMusic( MUSIC_FILE );
SimpleAudioEngine::getInstance()->preloadEffect( EFFECT_FILE );
virtual void playBackgroundMusic(const char* pszFilePath, bool bLoop = false); //播放背景音乐，bLoop表示是否要循环播放
virtual unsigned int playEffect(const char* pszFilePath, bool bLoop = false,
                                    float pitch = 1.0f, float pan = 0.0f, float gain = 1.0f); //播放音效，bLoop表示是否要循环播放
virtual void stopBackgroundMusic(bool bReleaseData = false); //停止背景音乐
virtual void stopEffect(unsigned int nSoundId); //停止指定音效，nSoundId为音效编号
virtual void stopAllEffects(); //停止所有音效

NSLog(@"test%@");


