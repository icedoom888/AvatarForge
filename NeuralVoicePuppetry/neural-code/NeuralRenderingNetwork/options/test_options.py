from .base_options import BaseOptions


class TestOptions(BaseOptions):
    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)
        parser.add_argument('--ntest', type=int, default=float("inf"), help='# of test examples.')
        parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
        parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        #  Dropout and Batchnorm has different behavioir during training and test.
        parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')
        parser.add_argument('--num_test', type=int, default=50, help='how many test images to run')

        parser.add_argument('--write_no_images', action='store_true', help='compute validation')

        parser.add_argument('--write_video', action='store_true', help='write video')
        parser.add_argument('--video_fps', type=float, default=25.0, help='video fps')

        parser.add_argument('--target_dataroot', type=str, default=None)
        parser.add_argument('--source_dataroot', type=str, default='./datasets/', help='loads source files (expressions, audio, uvs).')
        parser.add_argument('--expr_path', type=str, default=None)
        parser.add_argument('--images_target_dir', type=str, default=None, help='path to save images.')

        parser.add_argument('--frame_id_source', type=int, default=-1)
        parser.add_argument('--frame_id_target', type=int, default=-1)

        parser.set_defaults(model='test')
        # To avoid cropping, the loadSize should be the same as fineSize
        parser.set_defaults(loadSize=parser.get_default('fineSize'))
        self.isTrain = False
        return parser
