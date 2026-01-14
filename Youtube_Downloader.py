import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import threading
import os

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.download_path = os.path.expanduser("~/Downloads")
        self.quality_options = {}
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#1e1e1e")
        title_frame.pack(pady=20)
        
        title = tk.Label(title_frame, text="YouTube Video Downloader", 
                        font=("Helvetica", 24, "bold"), 
                        fg="#ff0000", bg="#1e1e1e")
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Download videos in any quality", 
                           font=("Helvetica", 10), 
                           fg="#888888", bg="#1e1e1e")
        subtitle.pack()
        
        # URL Input
        url_frame = tk.Frame(self.root, bg="#1e1e1e")
        url_frame.pack(pady=15, padx=40, fill="x")
        
        url_label = tk.Label(url_frame, text="Video URL:", 
                            font=("Helvetica", 11, "bold"), 
                            fg="#ffffff", bg="#1e1e1e")
        url_label.pack(anchor="w")
        
        self.url_entry = tk.Entry(url_frame, font=("Helvetica", 11), 
                                  bg="#2d2d2d", fg="#ffffff", 
                                  insertbackground="#ffffff", 
                                  relief="flat", bd=0)
        self.url_entry.pack(fill="x", ipady=8, pady=5)
        
        # Fetch Info Button
        fetch_btn = tk.Button(url_frame, text="Fetch Video Info", 
                             font=("Helvetica", 10, "bold"),
                             bg="#ff0000", fg="#ffffff", 
                             relief="flat", bd=0,
                             cursor="hand2",
                             command=self.fetch_info)
        fetch_btn.pack(pady=5)
        
        # Video Info Display
        info_frame = tk.Frame(self.root, bg="#2d2d2d")
        info_frame.pack(pady=10, padx=40, fill="both", expand=True)
        
        self.info_text = tk.Text(info_frame, height=6, 
                                font=("Helvetica", 9),
                                bg="#2d2d2d", fg="#ffffff", 
                                relief="flat", bd=0, wrap="word")
        self.info_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.info_text.config(state="disabled")
        
        # Quality Selection
        quality_frame = tk.Frame(self.root, bg="#1e1e1e")
        quality_frame.pack(pady=10, padx=40, fill="x")
        
        quality_label = tk.Label(quality_frame, text="Select Quality:", 
                                font=("Helvetica", 11, "bold"), 
                                fg="#ffffff", bg="#1e1e1e")
        quality_label.pack(anchor="w")
        
        self.quality_var = tk.StringVar()
        self.quality_combo = ttk.Combobox(quality_frame, 
                                         textvariable=self.quality_var,
                                         font=("Helvetica", 10),
                                         state="readonly")
        self.quality_combo.pack(fill="x", pady=5)
        
        # Download Path
        path_frame = tk.Frame(self.root, bg="#1e1e1e")
        path_frame.pack(pady=10, padx=40, fill="x")
        
        path_label = tk.Label(path_frame, text="Download Location:", 
                             font=("Helvetica", 11, "bold"), 
                             fg="#ffffff", bg="#1e1e1e")
        path_label.pack(anchor="w")
        
        path_inner = tk.Frame(path_frame, bg="#1e1e1e")
        path_inner.pack(fill="x")
        
        self.path_entry = tk.Entry(path_inner, font=("Helvetica", 9), 
                                   bg="#2d2d2d", fg="#ffffff",
                                   insertbackground="#ffffff", 
                                   relief="flat", bd=0)
        self.path_entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.path_entry.insert(0, self.download_path)
        
        browse_btn = tk.Button(path_inner, text="Browse", 
                              font=("Helvetica", 9, "bold"),
                              bg="#444444", fg="#ffffff", 
                              relief="flat", bd=0,
                              cursor="hand2",
                              command=self.browse_folder)
        browse_btn.pack(side="right", padx=(5, 0))
        
        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(self.root, variable=self.progress_var,
                                       maximum=100, mode='determinate')
        self.progress.pack(pady=10, padx=40, fill="x")
        
        # Status Label
        self.status_label = tk.Label(self.root, text="Ready", 
                                     font=("Helvetica", 9), 
                                     fg="#888888", bg="#1e1e1e")
        self.status_label.pack()
        
        # Download Button
        download_btn = tk.Button(self.root, text="Download Video", 
                                font=("Helvetica", 12, "bold"),
                                bg="#00ff00", fg="#000000", 
                                relief="flat", bd=0,
                                cursor="hand2",
                                command=self.start_download)
        download_btn.pack(pady=15, ipadx=40, ipady=10)
        
    def fetch_info(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        self.status_label.config(text="Fetching video information...")
        self.progress_var.set(0)
        
        thread = threading.Thread(target=self._fetch_info_thread, args=(url,))
        thread.start()
        
    def _fetch_info_thread(self, url):
        try:
            ydl_opts = {'quiet': True, 'no_warnings': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                self.info_text.config(state="normal")
                self.info_text.delete(1.0, tk.END)
                self.info_text.insert(tk.END, f"Title: {info.get('title', 'N/A')}\n")
                self.info_text.insert(tk.END, f"Duration: {info.get('duration', 0) // 60} min {info.get('duration', 0) % 60} sec\n")
                self.info_text.insert(tk.END, f"Uploader: {info.get('uploader', 'N/A')}\n")
                self.info_text.insert(tk.END, f"Views: {info.get('view_count', 'N/A'):,}\n")
                self.info_text.config(state="disabled")
                
                formats = info.get('formats', [])
                quality_dict = {}
                
                for f in formats:
                    if f.get('vcodec') != 'none' and f.get('acodec') != 'none':
                        height = f.get('height')
                        if height:
                            label = f"{height}p"
                            if label not in quality_dict:
                                quality_dict[label] = f['format_id']
                
                quality_dict['Best Quality'] = 'bestvideo+bestaudio/best'
                quality_dict['Audio Only (MP3)'] = 'bestaudio'
                
                self.quality_options = quality_dict
                self.quality_combo['values'] = list(quality_dict.keys())
                if quality_dict:
                    self.quality_combo.current(0)
                
                self.status_label.config(text="Video info fetched successfully!")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch video info: {str(e)}")
            self.status_label.config(text="Error fetching info")
            
    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_path = folder
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)
            
    def start_download(self):
        url = self.url_entry.get().strip()
        quality = self.quality_var.get()
        
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        if not quality:
            messagebox.showerror("Error", "Please select a quality")
            return
            
        self.download_path = self.path_entry.get()
        
        thread = threading.Thread(target=self._download_thread, args=(url, quality))
        thread.start()
        
    def _download_thread(self, url, quality):
        try:
            format_id = self.quality_options.get(quality, 'best')
            
            ydl_opts = {
                'format': format_id,
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
            }
            
            if quality == 'Audio Only (MP3)':
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            
            self.status_label.config(text="Downloading...")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            self.status_label.config(text="Download completed!")
            self.progress_var.set(100)
            messagebox.showinfo("Success", "Video downloaded successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {str(e)}")
            self.status_label.config(text="Download failed")
            self.progress_var.set(0)
            
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            if 'total_bytes' in d:
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                self.progress_var.set(percent)
            elif 'total_bytes_estimate' in d:
                percent = (d['downloaded_bytes'] / d['total_bytes_estimate']) * 100
                self.progress_var.set(percent)

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()