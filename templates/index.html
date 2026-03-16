import React, { useState } from 'react';
import { Search, Download, Youtube, Loader2, AlertCircle, Play, Clock, User, Shield, Globe, ChevronDown, Facebook, Twitter, Instagram } from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { PrivacyPolicy } from './components/PrivacyPolicy';
import { languages, translations, Language } from './translations';

interface VideoFormat {
  quality: string;
  container: string;
  url: string;
  hasVideo: boolean;
  hasAudio: boolean;
  itag?: number;
}

interface VideoInfo {
  title: string;
  thumbnail: string;
  duration: string;
  author: string;
  formats: VideoFormat[];
}

export default function App() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [videoInfo, setVideoInfo] = useState<VideoInfo | null>(null);
  const [showPrivacy, setShowPrivacy] = useState(false);
  const [lang, setLang] = useState<Language>('en');
  const [showLangMenu, setShowLangMenu] = useState(false);

  const t = translations[lang];

  const fetchVideoInfo = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!url) return;

    setLoading(true);
    setError(null);
    setVideoInfo(null);

    try {
      const response = await fetch(`/api/video-info?url=${encodeURIComponent(url)}`);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Failed to fetch video info');
      }

      setVideoInfo(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred');
    } finally {
      setLoading(false);
    }
  };

  const formatDuration = (seconds: string) => {
    const s = parseInt(seconds);
    const h = Math.floor(s / 3600);
    const m = Math.floor((s % 3600) / 60);
    const rs = s % 60;
    return `${h > 0 ? h + ':' : ''}${m.toString().padStart(2, '0')}:${rs.toString().padStart(2, '0')}`;
  };

  if (showPrivacy) {
    return (
      <div className="min-h-screen bg-zinc-50 flex flex-col items-center">
        <PrivacyPolicy onBack={() => setShowPrivacy(false)} />
        <footer className="mt-auto pb-12 text-zinc-400 text-sm">
          <p>© 2026 Turbo Video Downloader • The Best YouTube Downloader</p>
        </footer>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-zinc-50 flex flex-col items-center">
      {/* Navigation Bar */}
      <nav className="w-full bg-white border-b border-zinc-100 py-4 px-6 md:px-12 flex items-center justify-between sticky top-0 z-50">
        <div className="flex items-center gap-2">
          <div className="bg-red-600 p-1.5 rounded-lg">
            <Youtube className="w-5 h-5 text-white" />
          </div>
          <span className="text-xl font-bold text-zinc-900 tracking-tight">Turbo Video Downloader</span>
        </div>
        <div className="hidden md:flex items-center gap-8 text-sm font-medium text-zinc-600">
          <a href="#" className="text-red-600">{t.nav.downloader}</a>
          <a href="#" className="hover:text-red-600 transition-colors">{t.nav.mp3}</a>
          <a href="#" className="hover:text-red-600 transition-colors">{t.nav.mp4}</a>
          <a href="#" className="hover:text-red-600 transition-colors">{t.nav.facebook}</a>
        </div>
        
        <div className="relative">
          <button 
            onClick={() => setShowLangMenu(!showLangMenu)}
            className="flex items-center gap-2 text-sm font-bold text-zinc-600 hover:text-red-600 transition-colors px-3 py-2 rounded-xl hover:bg-zinc-50"
          >
            <Globe className="w-4 h-4" />
            <span className="uppercase">{lang}</span>
            <ChevronDown className={`w-3 h-3 transition-transform ${showLangMenu ? 'rotate-180' : ''}`} />
          </button>

          <AnimatePresence>
            {showLangMenu && (
              <motion.div
                initial={{ opacity: 0, y: 10, scale: 0.95 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                exit={{ opacity: 0, y: 10, scale: 0.95 }}
                className="absolute right-0 mt-2 w-48 bg-white border border-zinc-100 rounded-2xl shadow-2xl shadow-zinc-200/50 py-2 z-50 max-h-[70vh] overflow-y-auto"
              >
                {Object.entries(languages).map(([code, name]) => (
                  <button
                    key={code}
                    onClick={() => {
                      setLang(code as Language);
                      setShowLangMenu(false);
                    }}
                    className={`w-full text-left px-4 py-2.5 text-sm font-medium transition-colors hover:bg-red-50 hover:text-red-600 ${lang === code ? 'text-red-600 bg-red-50/50' : 'text-zinc-600'}`}
                  >
                    {name}
                  </button>
                ))}
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </nav>

      <main className="w-full max-w-5xl px-4 py-12 md:py-20 space-y-16">
        {/* Hero Section */}
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center space-y-6"
        >
          <div className="space-y-2">
            <h1 className="text-4xl md:text-5xl font-extrabold text-zinc-900 tracking-tight">
              {t.hero.title}
            </h1>
            <p className="text-zinc-500 text-lg md:text-xl max-w-2xl mx-auto">
              {t.hero.subtitle}
            </p>
          </div>

          <form onSubmit={fetchVideoInfo} className="relative max-w-3xl mx-auto group">
            <div className="absolute inset-y-0 left-0 pl-5 flex items-center pointer-events-none">
              <Search className="h-6 w-6 text-zinc-400 group-focus-within:text-red-500 transition-colors" />
            </div>
            <input
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder={t.hero.placeholder}
              className="block w-full pl-14 pr-36 py-5 bg-white border-2 border-zinc-100 rounded-2xl shadow-xl shadow-zinc-200/50 focus:ring-4 focus:ring-red-500/10 focus:border-red-500 outline-none transition-all text-zinc-800 text-lg placeholder:text-zinc-400"
            />
            <button
              type="submit"
              disabled={loading || !url}
              className="absolute right-2.5 top-2.5 bottom-2.5 px-8 bg-red-600 text-white rounded-xl font-bold hover:bg-red-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center gap-2 shadow-lg shadow-red-200"
            >
              {loading ? <Loader2 className="w-5 h-5 animate-spin" /> : (
                <>
                  <Download className="w-5 h-5" />
                  <span>{t.hero.button}</span>
                </>
              )}
            </button>
          </form>

          {/* Supported Platforms */}
          <div className="flex items-center justify-center gap-8 pt-4">
            <div className="flex flex-col items-center gap-2 group cursor-default">
              <div className="w-14 h-14 bg-white rounded-2xl shadow-lg shadow-zinc-200/50 flex items-center justify-center border border-zinc-100 group-hover:border-red-500 group-hover:scale-110 transition-all duration-300">
                <Youtube className="w-7 h-7 text-[#FF0000]" />
              </div>
              <span className="text-xs font-bold text-zinc-400 uppercase tracking-widest group-hover:text-zinc-600 transition-colors">YouTube</span>
            </div>
            <div className="flex flex-col items-center gap-2 group cursor-default">
              <div className="w-14 h-14 bg-white rounded-2xl shadow-lg shadow-zinc-200/50 flex items-center justify-center border border-zinc-100 group-hover:border-blue-600 group-hover:scale-110 transition-all duration-300">
                <Facebook className="w-7 h-7 text-[#1877F2]" />
              </div>
              <span className="text-xs font-bold text-zinc-400 uppercase tracking-widest group-hover:text-zinc-600 transition-colors">Facebook</span>
            </div>
            <div className="flex flex-col items-center gap-2 group cursor-default">
              <div className="w-14 h-14 bg-white rounded-2xl shadow-lg shadow-zinc-200/50 flex items-center justify-center border border-zinc-100 group-hover:border-black group-hover:scale-110 transition-all duration-300">
                <svg viewBox="0 0 24 24" className="w-7 h-7 fill-current text-black" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.59-1.01V14.5c.01 2.32-.6 4.67-2.12 6.44-1.56 1.82-3.9 2.89-6.27 3.05-2.47.16-5.06-.47-6.95-2.08-1.97-1.68-3.07-4.23-2.86-6.8.2-2.35 1.47-4.57 3.46-5.86 1.88-1.22 4.23-1.62 6.42-1.1v4.14c-1.3-.36-2.76-.23-3.93.45-.94.54-1.63 1.47-1.85 2.54-.22 1.07-.02 2.22.56 3.14.58.92 1.54 1.57 2.59 1.81 1.05.24 2.19.07 3.12-.47.93-.54 1.58-1.47 1.82-2.54.06-.25.09-.51.09-.77V.02z"/>
                </svg>
              </div>
              <span className="text-xs font-bold text-zinc-400 uppercase tracking-widest group-hover:text-zinc-600 transition-colors">TikTok</span>
            </div>
          </div>
        </motion.div>

        <AnimatePresence mode="wait">
          {error && (
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="max-w-3xl mx-auto bg-red-50 border border-red-100 p-4 rounded-2xl flex items-center gap-3 text-red-700"
            >
              <AlertCircle className="w-5 h-5 flex-shrink-0" />
              <p className="text-sm font-medium">{error}</p>
            </motion.div>
          )}

          {videoInfo && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="max-w-4xl mx-auto bg-white border border-zinc-100 rounded-[2.5rem] shadow-2xl shadow-zinc-200/50 overflow-hidden"
            >
              <div className="md:flex">
                <div className="md:w-2/5 relative aspect-video md:aspect-auto">
                  <img
                    src={videoInfo.thumbnail}
                    alt={videoInfo.title}
                    className="w-full h-full object-cover"
                    referrerPolicy="no-referrer"
                  />
                  <div className="absolute bottom-4 right-4 bg-black/80 text-white text-xs font-bold px-2.5 py-1.5 rounded-lg backdrop-blur-md">
                    {formatDuration(videoInfo.duration)}
                  </div>
                </div>
                <div className="p-8 md:w-3/5 space-y-6">
                  <div>
                    <h2 className="text-2xl font-bold text-zinc-900 line-clamp-2 leading-tight">
                      {videoInfo.title}
                    </h2>
                    <div className="flex items-center gap-4 mt-3 text-zinc-500 font-medium">
                      <span className="flex items-center gap-1.5">
                        <User className="w-4 h-4" />
                        {videoInfo.author}
                      </span>
                    </div>
                  </div>

                  <div className="space-y-4">
                    <p className="text-xs font-black text-zinc-400 uppercase tracking-[0.2em]">Select Quality</p>
                    <div className="grid grid-cols-1 gap-3">
                      {videoInfo.formats
                        .filter(f => f.hasVideo && f.hasAudio)
                        .slice(0, 5)
                        .map((format, idx) => (
                        <a
                          key={idx}
                          href={`/api/download?url=${encodeURIComponent(url)}&itag=${format.itag}`}
                          className="flex items-center justify-between p-4 rounded-2xl border border-zinc-100 hover:border-red-500 hover:bg-red-50 transition-all group"
                        >
                          <div className="flex items-center gap-4">
                            <div className="w-10 h-10 bg-zinc-50 rounded-xl flex items-center justify-center group-hover:bg-red-100 transition-colors">
                              <Play className="w-5 h-5 text-zinc-600 group-hover:text-red-600" />
                            </div>
                            <div>
                              <p className="font-bold text-zinc-900">{format.quality || 'Auto'}</p>
                              <p className="text-xs text-zinc-500 font-bold uppercase tracking-wider">{format.container}</p>
                            </div>
                          </div>
                          <div className="flex items-center gap-2 text-red-600 font-bold text-sm opacity-0 group-hover:opacity-100 transition-opacity">
                            <span>Download</span>
                            <Download className="w-4 h-4" />
                          </div>
                        </a>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* How to Download Section */}
        <section className="space-y-10 pt-10">
          <div className="text-center space-y-2">
            <h2 className="text-3xl font-bold text-zinc-900">{t.howTo.title}</h2>
            <p className="text-zinc-500">{t.howTo.subtitle}</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              { step: '01', title: t.howTo.steps.step1.title, desc: t.howTo.steps.step1.desc },
              { step: '02', title: t.howTo.steps.step2.title, desc: t.howTo.steps.step2.desc },
              { step: '03', title: t.howTo.steps.step3.title, desc: t.howTo.steps.step3.desc }
            ].map((item, i) => (
              <div key={i} className="relative p-8 bg-white border border-zinc-100 rounded-3xl shadow-sm space-y-4">
                <span className="text-5xl font-black text-zinc-100 absolute top-4 right-6 select-none">{item.step}</span>
                <h3 className="text-xl font-bold text-zinc-900 relative z-10">{item.title}</h3>
                <p className="text-zinc-500 leading-relaxed relative z-10">{item.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Features Section */}
        <section className="space-y-10">
          <div className="text-center space-y-2">
            <h2 className="text-3xl font-bold text-zinc-900">{t.features.title}</h2>
            <p className="text-zinc-500">{t.features.subtitle}</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[
              { icon: Play, title: t.features.items.simple.title, desc: t.features.items.simple.desc },
              { icon: Shield, title: t.features.items.free.title, desc: t.features.items.free.desc },
              { icon: Youtube, title: t.features.items.quality.title, desc: t.features.items.quality.desc },
              { icon: Clock, title: t.features.items.fast.title, desc: t.features.items.fast.desc },
              { icon: Search, title: t.features.items.cross.title, desc: t.features.items.cross.desc },
              { icon: Download, title: t.features.items.unlimited.title, desc: t.features.items.unlimited.desc }
            ].map((feature, i) => (
              <div key={i} className="p-8 bg-white border border-zinc-100 rounded-3xl hover:shadow-xl hover:shadow-zinc-200/50 transition-all space-y-4 group">
                <div className="w-12 h-12 bg-red-50 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                  <feature.icon className="w-6 h-6 text-red-600" />
                </div>
                <h3 className="text-lg font-bold text-zinc-900">{feature.title}</h3>
                <p className="text-sm text-zinc-500 leading-relaxed">{feature.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* FAQ Section Placeholder */}
        <section className="bg-zinc-900 rounded-[3rem] p-10 md:p-16 text-white space-y-10">
          <div className="text-center space-y-2">
            <h2 className="text-3xl font-bold">{t.faq.title}</h2>
            <p className="text-zinc-400">{t.faq.subtitle}</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="space-y-3">
              <h4 className="font-bold text-red-500">{t.faq.q1.q}</h4>
              <p className="text-zinc-400 text-sm leading-relaxed">{t.faq.q1.a}</p>
            </div>
            <div className="space-y-3">
              <h4 className="font-bold text-red-500">{t.faq.q2.q}</h4>
              <p className="text-zinc-400 text-sm leading-relaxed">{t.faq.q2.a}</p>
            </div>
            <div className="space-y-3">
              <h4 className="font-bold text-red-500">{t.faq.q3.q}</h4>
              <p className="text-zinc-400 text-sm leading-relaxed">{t.faq.q3.a}</p>
            </div>
            <div className="space-y-3">
              <h4 className="font-bold text-red-500">{t.faq.q4.q}</h4>
              <p className="text-zinc-400 text-sm leading-relaxed">{t.faq.q4.a}</p>
            </div>
          </div>
        </section>
      </main>
      
      <footer className="w-full bg-white border-t border-zinc-100 py-12 px-6 flex flex-col items-center gap-6">
        <div className="flex items-center gap-2">
          <div className="bg-red-600 p-1.5 rounded-lg">
            <Youtube className="w-5 h-5 text-white" />
          </div>
          <span className="text-xl font-bold text-zinc-900 tracking-tight">Turbo Video Downloader</span>
        </div>
        <div className="flex flex-wrap justify-center gap-6 text-sm font-medium text-zinc-500">
          <a href="#" className="hover:text-red-600 transition-colors">{t.footer.terms}</a>
          <button 
            onClick={() => setShowPrivacy(true)}
            className="hover:text-red-600 transition-colors"
          >
            {t.footer.privacy}
          </button>
          <a href="#" className="hover:text-red-600 transition-colors">{t.footer.contact}</a>
        </div>
        <div className="flex items-center gap-4">
          <a href="#" className="w-10 h-10 flex items-center justify-center rounded-full bg-zinc-100 text-zinc-600 hover:bg-red-600 hover:text-white transition-all duration-300">
            <Facebook className="w-5 h-5" />
          </a>
          <a href="#" className="w-10 h-10 flex items-center justify-center rounded-full bg-zinc-100 text-zinc-600 hover:bg-red-600 hover:text-white transition-all duration-300">
            <Twitter className="w-5 h-5" />
          </a>
          <a href="#" className="w-10 h-10 flex items-center justify-center rounded-full bg-zinc-100 text-zinc-600 hover:bg-red-600 hover:text-white transition-all duration-300">
            <Instagram className="w-5 h-5" />
          </a>
          <a href="#" className="w-10 h-10 flex items-center justify-center rounded-full bg-zinc-100 text-zinc-600 hover:bg-red-600 hover:text-white transition-all duration-300">
            <Youtube className="w-5 h-5" />
          </a>
        </div>
        <p className="text-zinc-400 text-xs">{t.footer.copyright}</p>
      </footer>
    </div>
  );
}
