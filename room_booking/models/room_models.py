from odoo import models, fields, api

class MasterRuangan(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    nama_ruangan = fields.Char(string='Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('kecil', 'Meeting Room Kecil'),
        ('besar', 'Meeting Room Besar'),
        ('aula', 'Aula')],
        string='Tipe Ruangan', required=True
    )
    lokasi_ruangan = fields.Selection([
        ('1A', '1A'), ('1B', '1B'), ('1C', '1C'),
        ('2A', '2A'), ('2B', '2B'), ('2C', '2C')],
        string='Lokasi Ruangan', required=True
    )
    foto_ruangan = fields.Binary(string='Foto Ruangan', required=True)
    kapasitas = fields.Integer(string='Kapasitas', required=True)
    keterangan = fields.Text(string='Keterangan')

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string='Nomor Pemesanan', required=True)
    ruangan_id = fields.Many2one('master.ruangan', string='Ruangan', required=True)
    nama_pemesan = fields.Char(string='Nama Pemesan', required=True)
    tanggal_pemesanan = fields.Date(string='Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done')],
        string='Status Pemesanan', default='draft'
    )
    catatan_pemesanan = fields.Text(string='Catatan')

    _sql_constraints = [
        ('unique_nama_pemesan', 'UNIQUE(nama_pemesan)', 'Nama Pemesan harus unik!'),
        ('unique_ruangan_date', 'UNIQUE(ruangan_id, tanggal_pemesanan)', 'Ruangan sudah dipesan di tanggal ini!')
    ]

    @api.multi
    def proses_pemesanan(self):
        self.status_pemesanan = 'on_going'

    @api.multi
    def selesai_pemesanan(self):
        self.status_pemesanan = 'done'
